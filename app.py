from dotenv import load_dotenv
import streamlit as st
from openai import OpenAI
import os
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from sentence_transformers import SentenceTransformer
from weaviate import Client
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import uuid as uuid_lib
import weaviate


tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
transformer_model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")
sentence_transformer_model = SentenceTransformer('paraphrase-distilroberta-base-v1')
                                                                    
load_dotenv()
openai_api_key = os.environ["OPENAI_API_KEY"]
api_key = os.environ["AUTHENTICATION_APIKEY_ALLOWED_KEYS"]
api_user = os.environ["AUTHENTICATION_APIKEY_USERS"]

if openai_api_key is None:                                          
    raise ValueError("OpenAI API-Schlüssel wurde nicht gefunden. Bitte setzen Sie die Umgebungsvariable 'OPENAI_API_KEY'.")
                                                                             
# Instantiate the client with the auth config
client = Client(
    url="http://148.251.184.47:8090",  # Replace w/ your endpoint
    auth_client_secret=weaviate.AuthApiKey(api_key=api_key),  # Replace w/ your Weaviate instance API key
)

GPTClient = OpenAI()


# Überprüfen Sie, ob die Klasse existiert, bevor Sie sie löschen
existing_classes = client.schema.get()['classes']

if any(_class['class'] == 'Author' for _class in existing_classes):
    client.schema.delete_class('Author')

schema = {
    "classes": [
        {
            "class": "Author",
            "properties": [
                {
                    "name": "text",
                    "dataType": ["text"],
                }
            ]
        }
    ]
}

client.schema.delete_all()
client.schema.create(schema)

def ask_gpt(question, documents):
    # Formulieren Sie die Nachrichten für die Chat-Anfrage
    messages = [
        {"role": "system", "content": "Bitte beantworte auf die folgende Frage:"},
        {"role": "user", "content": question}
    ]

    # Fügen Sie den Kontext aus den Dokumenten hinzu
    for doc in documents:
        messages.append({"role": "system", "content": doc})

    # Senden Sie die Anfrage an OpenAI
    response = GPTClient.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=messages
    )

    # Geben Sie die Antwort zurück
    return response.choices[0].message.content


class SentenceTransformerEmbeddings:
    def embed_documents(self, texts):
        return sentence_transformer_model .encode(texts)

    def embed_query(self, query):
        return sentence_transformer_model .encode([query])[0]
    
def retrieve_document(uuid):
    with open('documents.txt', 'r') as f:
        for line in f:
            if line.startswith(uuid):
                return line[len(uuid)+2:].strip()  # return the document text without the uuid and newline

def truncate_to_max_length(tokenizer, text, max_length):
    # Tokenize the text with truncation and return token IDs
    tokens = tokenizer.encode(text, add_special_tokens=True, truncation=True, max_length=max_length)
    return tokens


   
def main():
    st.set_page_config(page_title="AI-Driven DocChat", layout="wide")
    st.title("AI-Driven DocChat: Powered by Weaviate and OpenAI")

    # Upload-Bereich für PDF-Dateien
    file = st.sidebar.file_uploader("Upload your PDF", type=["pdf"])
    st.sidebar.markdown("---")

    hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
.stDeployButton {visibility: hidden;}
</style>

"""
   
    uuids = []

    if file:
        # PDF verarbeiten
        pdf_reader = PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() or ""

        # Text in Chunks unterteilen
        text_splitter = CharacterTextSplitter(separator="\n", chunk_size=1000, chunk_overlap=200, length_function=len)
        chunks = text_splitter.split_text(text)

        # Chunks in Weaviate speichern und UUIDs sammeln
        for chunk in chunks:
            chunk_uuid = str(uuid_lib.uuid4())
            client.data_object.create(data_object={"text": chunk}, class_name="Document", uuid=chunk_uuid)
            uuids.append(chunk_uuid)

        # Benutzerabfrage
        user_question = st.sidebar.text_input("Ask a question about the document:")

        # Layout mit zwei Spalten
        col1, col2 = st.columns((2, 1))

        if user_question:
            # Weaviate-Suche durchführen
            search_results = client.query.get('Document', ['text']).with_near_text({"concepts": [user_question]}).with_limit(5).do()
            docs = [obj['text'] for obj in search_results['data']['Get']['Document']]

            # Linke Spalte: Antwort von GPT-3
            with col1:
                gpt_answer = ask_gpt(user_question, docs)
                st.subheader("Answer from ChatGPT:")
                st.write(gpt_answer)

            # Rechte Spalte: Weaviate Suchergebnisse und Dokumenten-Chunks
            with col2:
                st.subheader("Weaviate Search Results:")
                for doc in docs:
                    st.write(doc)

                st.subheader("Document Chunks:")
                for i, chunk in enumerate(chunks):
                    st.write(f"Chunk {i+1}: {chunk[:50]}...")

                st.subheader("Chunk UUIDs:")
                for uuid in uuids:
                    st.write(uuid)
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 


    st.sidebar.markdown("### About this App")
    st.sidebar.info("Developed by Keyvan Hardani, this application combines Weaviate's vector search with OpenAI's GPT-4 for sophisticated document analysis. Users can upload PDF documents and ask context-specific questions, which are answered using advanced search and AI-driven response mechanisms.")

if __name__ == '__main__':
    main()

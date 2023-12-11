# AI-Driven DocChat: Powered by Weaviate and OpenAI

## Overview
AI-Driven DocChat is an innovative application that combines Weaviate's vector search with OpenAI's GPT-4, offering an interactive and efficient tool for document analysis. It allows users to upload PDF documents and ask context-related questions, answered through AI-powered search and response mechanisms.

## Key Features
- **PDF Analysis**: Process and extract text from uploaded PDF documents.
- **Text Splitting**: Divide text into manageable chunks for more efficient processing.
- **Weaviate Vector Search**: Search document chunks using Weaviate's vector search capabilities to find relevant sections.
- **GPT-4-based Responses**: Generate responses to user queries using OpenAI's GPT-4, supported by the context from Weaviate search results.

## Technologies
- **Weaviate**: An AI-powered vector search and storage mechanism.
- **OpenAI GPT-4**: An advanced language processing model providing deep insights and responses.
- **Streamlit**: A powerful library for building web applications.
- **PyPDF2 & Langchain**: Tools for reading and processing PDF content.
- **Sentence Transformers**: For efficient sentence encoding and semantic similarity search.

## Installation and Usage
1. Clone the repository.
2. Install required libraries with `pip install -r requirements.txt`.
3. Start the Streamlit application with `streamlit run app.py`.
4. Upload a PDF and ask questions through the sidebar.

## Note
Ensure you have valid API keys for OpenAI and Weaviate to fully utilize the application's functionality.

## License
This project is under the [MIT License](LICENSE).

---

*This project uses OpenAI's GPT-4 for language processing and Weaviate for vector search.*

# AI-Driven DocChat: Powered by Weaviate and OpenAI

## Überblick
AI-Driven DocChat ist eine innovative Anwendung, die Weaviates Vektorsuche mit der Leistungsfähigkeit von OpenAI's GPT-4 kombiniert, um ein interaktives und effizientes Werkzeug für die Dokumentanalyse zu bieten. Diese Anwendung ermöglicht es Benutzern, PDF-Dokumente hochzuladen und kontextbezogene Fragen zu stellen, die durch KI-gestützte Such- und Antwortmechanismen beantwortet werden.

## Hauptmerkmale
- **PDF-Analyse**: Verarbeiten und Extrahieren von Text aus hochgeladenen PDF-Dokumenten.
- **Textsplitting**: Unterteilung des Textes in verwaltbare Chunks für effizientere Verarbeitung.
- **Weaviate-Vektorsuche**: Durchsuchen der Dokumenten-Chunks mit Weaviates Vektorsuchfunktionen, um relevante Abschnitte zu finden.
- **GPT-4-basierte Antworten**: Generieren von Antworten auf Benutzerfragen unter Verwendung von OpenAI's GPT-4, unterstützt durch den Kontext der Weaviate-Suchergebnisse.

## Technologien
- **Weaviate**: Ein KI-gestützter Vektorsuch- und Speichermechanismus.
- **OpenAI GPT-4**: Ein fortschrittliches Sprachverarbeitungsmodell, das tiefgreifende Einsichten und Antworten liefert.
- **Streamlit**: Eine leistungsstarke Bibliothek zur Erstellung von Webanwendungen.
- **PyPDF2 & Langchain**: Werkzeuge zum Lesen und Bearbeiten von PDF-Inhalten.
- **Sentence Transformers**: Für effiziente Satzcodierung und semantische Ähnlichkeitssuche.

## Installation und Verwendung
1. Klone das Repository.
2. Installiere erforderliche Bibliotheken mit `pip install -r requirements.txt`.
3. Starte die Streamlit-Anwendung mit `streamlit run app.py`.
4. Lade ein PDF hoch und stelle Fragen über die Seitenleiste.

## Hinweis
Stelle sicher, dass du über gültige API-Schlüssel für OpenAI und Weaviate verfügst, um die volle Funktionalität der Anwendung zu nutzen.

## Mitwirkende
- [Dein Name/GitHub-Link]

## Lizenz
Dieses Projekt steht unter der [MIT-Lizenz](LICENSE).

---

*Dieses Projekt verwendet OpenAI's GPT-4 für die Sprachverarbeitung und Weaviate für die Vektorsuche.*

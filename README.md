# 👽 RAG PDFBot — Source Citations

A PDF-based Retrieval-Augmented Generation (RAG) chatbot built with FastAPI and Streamlit.

The application allows users to upload PDF documents, ask questions about their content, and receive answers generated from retrieved document context. This version extends the application with source citations, allowing users to verify the document, page, and relevant snippet behind each response.

---

## 🔗 Quick Links

<details>
<summary>Click to expand</summary>

- 🎥 Demo
- 🚀 Features
- 🧩 My Contributions
- 🏗️ Architecture
- 🛠️ Tech Stack
- 📦 Installation
- ▶️ Run the Application
- 📚 Source Citations

</details>

---

## 🎥 Demo

This demo shows the application processing a PDF, answering a question using retrieved document context, and displaying Sources & References with the document name, page number, and retrieved snippets.

### ▶️ Watch RAG PDFBot Demo

https://drive.google.com/file/d/1fIOv-A6Nie99S86Pt7CsvkpZC2CNhzsB/view?usp=sharing

---

## 🚀 Features

- 📁 Upload and process multiple PDF documents
- 💬 Ask questions about uploaded documents
- 🧠 Retrieval-Augmented Generation using LangChain
- 🔎 Semantic document retrieval using ChromaDB
- 📚 Source citations for generated responses
- 📄 Page-level source references
- 📝 Retrieved document snippets
- 🔌 Groq and Google Gemini model support
- 📦 Streamlit frontend
- ⚡ FastAPI backend
- 🔬 Vectorstore inspector
- 💾 Downloadable chat history
- 🔄 Reset, clear, and undo chat operations
- 🌐 API-driven frontend/backend communication
- 🧪 Token-based document chunking

---

## 🧩 My Contributions

The primary enhancement implemented in this project is source citations and grounding for RAG responses.

| Enhancement | Implementation |
|------------|----------------|
| 📚 Source Citations | Added retrieved document references to generated responses |
| 📄 Page References | Added user-facing page numbers for retrieved sources |
| 📝 Source Snippets | Displayed relevant retrieved text alongside citations |
| ⚡ API Response | Extended the FastAPI chat response with source metadata |
| 🖥️ Streamlit UI | Added a Sources & References section to chat responses |
| 💾 Chat History | Preserved source information in session history and CSV exports |
| 🔧 Groq Compatibility | Updated the Groq model configuration |
| 🔧 Gemini Compatibility | Updated the Gemini embedding configuration |
| 🔐 Environment Config | Improved .env loading from the project root |

### Citation Flow

    User Question
          │
          ▼
    ┌─────────────────┐
    │ Document        │
    │ Retrieval       │
    └────────┬────────┘
             │
             ▼
    ┌─────────────────┐
    │ Retrieved       │
    │ Document Chunks │
    └────────┬────────┘
             │
             ▼
    ┌─────────────────┐
    │ LLM Generation  │
    └────────┬────────┘
             │
             ▼
    ┌─────────────────────────┐
    │ Answer + Source Metadata│
    └────────────┬────────────┘
                 │
                 ▼
          Sources & References
           ├── Document
           ├── Page
           └── Snippet

---

## 🏗️ Architecture

    ┌──────────────────────────────┐
    │        Streamlit UI          │
    │          Frontend            │
    └──────────────┬───────────────┘
                   │
                   │ HTTP Requests
                   ▼
    ┌──────────────────────────────┐
    │          FastAPI             │
    │          Backend             │
    └──────────────┬───────────────┘
                   │
           ┌───────┴────────┐
           │                │
           ▼                ▼
    ┌──────────────┐  ┌───────────────┐
    │ PDF          │  │ ChromaDB      │
    │ Processing   │  │ Vector Store  │
    └──────┬───────┘  └───────┬───────┘
           │                  │
           ▼                  ▼
    ┌────────────────────────────────┐
    │        Document Retrieval       │
    └───────────────┬────────────────┘
                    │
                    ▼
    ┌────────────────────────────────┐
    │       LLM Answer Generation    │
    └───────────────┬────────────────┘
                    │
                    ▼
    ┌────────────────────────────────┐
    │ Answer + Source Citations      │
    │ Document • Page • Snippet      │
    └────────────────────────────────┘

---

## 🛠️ Tech Stack

<details>
<summary>Click to expand</summary>

### Frontend

- Streamlit — Interactive chat interface and source citation display

### Backend

- FastAPI — REST API and backend request handling
- Uvicorn — ASGI application server

### RAG / AI

- LangChain — Retrieval and LLM orchestration
- Groq — LLM provider
- Google Gemini — LLM and embedding provider

### Vector Database

- ChromaDB — Stores and retrieves document embeddings

### Embeddings

- HuggingFace Embeddings
- Google Gemini Embeddings

### Document Processing

- PyPDF — PDF text extraction
- TokenTextSplitter — Document chunking

### Language

- Python

</details>

---

## 📦 Installation

### 1. Clone the repository

    git clone https://github.com/Srilekha0629/Rag-Source-Citations.git
    cd Rag-Source-Citations

### 2. Create a virtual environment

#### Windows

    python -m venv venv
    venv\Scripts\activate

#### macOS / Linux

    python3 -m venv venv
    source venv/bin/activate

### 3. Install dependencies

Install backend dependencies:

    cd server
    pip install -r requirements.txt

Return to the project root:

    cd ..

Install frontend dependencies:

    cd client
    pip install -r requirements.txt

Return to the project root:

    cd ..

---

## 🔐 API Keys

The application requires API keys for the supported providers.

### Groq

Create an API key from:

https://console.groq.com/

### Google Gemini

Create an API key from:

https://ai.google.dev/

Create a .env file in the project root:

    GROQ_API_KEY=your-groq-api-key
    GOOGLE_API_KEY=your-google-api-key

> ⚠️ Never commit your .env file or expose API keys publicly.

---

## ▶️ Run the Application

The application uses two processes.

### Terminal 1 — FastAPI Backend

From the project root:

    cd server
    python -m uvicorn main:app --reload

Backend:

    http://127.0.0.1:8000

### Terminal 2 — Streamlit Frontend

Open another terminal:

    cd client
    python -m streamlit run app.py

Frontend:

    http://localhost:8501

---

## 💬 How to Use

1. Launch the FastAPI backend.
2. Launch the Streamlit frontend.
3. Select an available model provider.
4. Select a model.
5. Upload one or more PDF documents.
6. Wait for document processing to complete.
7. Ask a question about the uploaded documents.
8. Review the generated answer.
9. Expand Sources & References to inspect the retrieved sources.

---

## 📚 Source Citations

Each generated response can display the retrieved source information.

    ┌──────────────────────────────────────┐
    │ Answer                               │
    │                                      │
    │ Retrieval-Augmented Generation...    │
    │                                      │
    ├──────────────────────────────────────┤
    │ 📚 Sources & References              │
    │                                      │
    │ 📄 RAG_Test_Document.pdf             │
    │ Page: 3                              │
    │                                      │
    │ "Retrieval-Augmented Generation,     │
    │ or RAG, combines document retrieval  │
    │ with a language model..."            │
    └──────────────────────────────────────┘

The citation information includes:

- 📄 Source document name
- 🔢 Page number
- 📝 Retrieved text snippet

This makes generated responses easier to verify against the uploaded document.

---

## 🔬 Vectorstore Inspector

The application includes a vectorstore inspector that can be used to examine retrieved document chunks and understand the information being selected for a query.

This is useful for debugging and understanding RAG retrieval behavior.

---

## 🧰 Chat Tools

| Tool | Function |
|------|----------|
| 🔄 Reset | Resets the current application session |
| 🧹 Clear Chat | Clears the current conversation |
| ↩️ Undo | Removes the latest question and response |
| 💾 Download | Exports chat history as CSV |

---

## 📊 Chat History

Chat history can be exported as a CSV file.

The exported history includes source information.

| Question | Answer | Provider | Model | PDF File | Timestamp | Sources |
|----------|--------|----------|-------|----------|-----------|---------|
| What is RAG? | RAG combines... | Groq | GPT OSS 20B | document.pdf | Timestamp | document.pdf - Page 3 |

---

## 📁 Project Structure

<details>
<summary>Click to expand</summary>

    Rag-Source-Citations/
    │
    ├── client/                         # Streamlit Frontend
    │   ├── app.py                      # Main Streamlit entrypoint
    │   ├── components/
    │   │   ├── chat.py                 # Chat UI and source citations
    │   │   ├── inspector.py            # Vectorstore inspector
    │   │   └── sidebar.py              # Model and PDF controls
    │   ├── state/
    │   │   └── session.py              # Session state
    │   ├── utils/
    │   │   ├── api.py                  # Backend API communication
    │   │   ├── config.py               # Frontend configuration
    │   │   └── helpers.py              # Helper functions
    │   └── requirements.txt
    │
    ├── server/                         # FastAPI Backend
    │   ├── api/
    │   │   ├── routes.py               # API endpoints
    │   │   └── schemas.py              # Request/response schemas
    │   ├── core/
    │   │   ├── document_processor.py   # PDF processing and chunking
    │   │   ├── llm_chain_factory.py    # LLM and retrieval chain
    │   │   └── vector_database.py      # Embeddings and ChromaDB
    │   ├── config/
    │   │   └── settings.py             # Application configuration
    │   ├── utils/
    │   │   └── logger.py               # Logging
    │   ├── main.py                     # FastAPI entrypoint
    │   └── requirements.txt
    │
    ├── data/                           # Vectorstore data
    ├── temp/                           # Temporary files
    ├── .env                            # Local API keys
    ├── .gitignore
    └── README.md

</details>

---

## 🔒 Security

- 🔐 API keys are stored in .env
- 🚫 .env is excluded from Git
- 🔑 API keys should never be committed to the repository
- 📸 Do not expose API keys in screenshots or demo videos
- 🌐 Keep API credentials private when deploying the application

---

## 🙏 Technologies

This project uses the following technologies and open-source tools:

- LangChain
- Streamlit
- FastAPI
- Groq
- Google AI
- ChromaDB
- Hugging Face

---

## 🎯 Project Focus

The primary enhancement in this version is **source citations for RAG responses**.

The implementation provides:

- 📄 Document-level attribution
- 🔢 Page-level references
- 📝 Retrieved text snippets
- 🖥️ Source display in the Streamlit interface
- 💾 Source information in chat history
- 📊 Source information in CSV exports

The goal is to make RAG responses more transparent by allowing users to inspect the document context retrieved for each answer.

---

⭐ If you find this project useful, feel free to explore the repository and experiment with the RAG pipeline.

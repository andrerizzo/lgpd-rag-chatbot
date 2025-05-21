# 💬 RAG-LGPD-Chatbot

A modular Question-Answering system on Brazil’s LGPD (General Data Protection Law), built using LangChain, ChromaDB, OpenAI, and Gradio.  
Ideal for legal assistant applications, compliance analysis, and document-based support.

---

## 📌 Overview

This project implements a complete Retrieval-Augmented Generation (RAG) pipeline with the following steps:

1. **PDF ingestion** of legal documents (e.g., LGPD)
2. **Document chunking** for semantic granularity
3. **Embedding generation** using OpenAI models
4. **Persistent vector storage** using ChromaDB
5. **Conversational chain construction** with memory via LangChain
6. **Interactive chat interface** powered by Gradio

---

## 🧱 Project Structure

```
.
├── app.py                    # Main execution script
├── data/                     # Folder for PDF documents (LGPD, etc.)
├── .env                      # OpenAI API Key file
├── src/
│   ├── config.py             # Configuration and parameters
│   ├── utils.py              # Helper functions (hash, etc.)
│   ├── loader.py             # PDF document loader
│   ├── splitter.py           # Text chunking
│   ├── embedding.py          # OpenAI embeddings
│   ├── vectorstore.py        # Chroma vector DB handler
│   ├── retriever.py          # Retriever configuration
│   └── langchain_layer.py    # Conversational chain builder
```

---

## 🚀 How to Run

1. **Install dependencies:**

```bash
pip install -r requirements.txt
```

2. **Create a `.env` file:**

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

3. **Add PDF files to the `data/` folder**

4. **Run the project:**

```bash
python app.py
```

5. **Access the interactive chat UI in your browser.**

---

## 🧠 Technologies Used

- [LangChain](https://python.langchain.com/)
- [OpenAI Embeddings](https://platform.openai.com/)
- [Chroma Vector DB](https://www.trychroma.com/)
- [Gradio](https://www.gradio.app/)
- [Python 3.10+](https://www.python.org/)

---

## ✅ Key Features

- Support for multiple PDF documents
- Memory-preserving chat history
- Modular and testable pipeline
- Easily extendable to other laws or domains (e.g., compliance, HR, healthcare)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🤝 Contributions

Pull requests are welcome. For suggestions, questions, or bugs, please open an issue.

---

## Author

Developed by **André Rizzo** — [LinkedIn](https://www.linkedin.com/in/andrerizzo1)

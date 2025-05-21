"""
Script principal do projeto RAG com LangChain, Chroma e Gradio.

Este script orquestra o pipeline completo:
1. Carregamento de documentos
2. Chunking com sobreposição
3. Geração de embeddings
4. Armazenamento no banco vetorial Chroma
5. Criação de uma cadeia conversacional com LangChain
6. Interface de chat interativa com Gradio

Requer configuração via arquivo .env para a chave da OpenAI.

Execução:
    python main.py
"""

from src.config import *
from src.loader import load_documents
from src.splitter import split_documents
from src.embedder import apply_embedding
from src.vectorstore import store_embeddings
from src.chain import build_chain
import gradio as gr
import os

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

# Ingestão
docs = load_documents(DATA_DIR)
chunks = split_documents(docs, CHUNK_SIZE, CHUNK_OVERLAP)
embedding = apply_embedding(EMBEDDING_MODEL)
vectorstore = store_embeddings(chunks, embedding, DB_NAME)

# Construção da chain
conversation_chain = build_chain(vectorstore, LLM_MODEL)

def chat(message, history):
    response = conversation_chain.invoke({"question": message})
    return response['answer']

view = gr.ChatInterface(chat).launch()
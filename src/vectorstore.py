import os
import shutil
from langchain_chroma import Chroma

def store_embeddings(chunks, embedding, persist_directory):
    """
    Armazena chunks vetorizados no ChromaDB.

    Parameters:
        chunks (list): Lista de chunks.
        embedding: Modelo de embeddings.
        persist_directory (str): Diretório de armazenamento.

    Returns:
        Chroma: Banco vetorial criado.
    """
    if os.path.exists(persist_directory):
        Chroma(persist_directory=persist_directory, embedding_function=embedding).delete_collection()
        shutil.rmtree(persist_directory)
    vectorstore = Chroma.from_documents(chunks, embedding, persist_directory=persist_directory)
    print(f"Banco de dados {persist_directory} gerado e embeddings carregados com sucesso")
    return vectorstore
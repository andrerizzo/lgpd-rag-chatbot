from langchain_openai.embeddings import OpenAIEmbeddings
from src.config import *

def apply_embedding(EMBEDDING_MODEL):
    """
    Inicializa e retorna um modelo de embeddings da OpenAI.

    Parameters:
        EMBEDDING_MODEL (str): Nome do modelo OpenAI a ser utilizado para geração dos embeddings.
                               Exemplo: "text-embedding-3-small" ou "text-embedding-3-large".

    Returns:
        OpenAIEmbeddings: Objeto de embedding compatível com LangChain, pronto para uso em vetorização de documentos.
    """
    
    return OpenAIEmbeddings(model=EMBEDDING_MODEL)
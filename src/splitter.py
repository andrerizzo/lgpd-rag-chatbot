
from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_documents(docs, CHUNK_SIZE=1000, CHUNK_OVERLAP=50):
    """
    Divide documentos em trechos (chunks) menores para uso em pipelines 
    de NLP ou RAG.

    Utiliza o RecursiveCharacterTextSplitter para segmentar os documentos 
    mantendo coerência textual, respeitando o tamanho definido e a 
    sobreposição entre os trechos.

    Parameters:
        docs (list): Lista de documentos (Document) a serem divididos.
        chunk_size (int, optional): Tamanho máximo de cada chunk. 
        Padrão é 1000 caracteres.
        chunk_overlap (int, optional): Número de caracteres de 
        sobreposição entre chunks. Padrão é 50.
    """
    
    splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE,
                                            chunk_overlap=CHUNK_OVERLAP)
    splitted_docs = splitter.split_documents(docs)
    print(f"Total de chunks gerados: {len(splitted_docs)}")
    
    return splitted_docs
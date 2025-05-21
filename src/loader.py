
import os
import hashlib
from datetime import datetime
from langchain_community.document_loaders import PyPDFLoader
from .utils import generate_doc_id

def load_documents(datadir):
    """
    Carrega documentos PDF de um diretório para uso em um pipeline 
    RAG (Retrieval-Augmented Generation).

    Esta função percorre recursivamente o diretório especificado, 
    identifica arquivos PDF, carrega seu conteúdo usando o PyPDFLoader 
    e adiciona metadados úteis, como caminho do arquivo, nome, tipo, 
    identificador único e data de ingestão.

    Parameters:
        datadir (str): Caminho do diretório onde os arquivos PDF estão 
        armazenados.

    Returns:
        list: Lista de documentos carregados com metadados, prontos 
        para processamento em um sistema RAG.
    """
    
    docs = []

    ### Carrega arquivos
    for root, _,files in os.walk(datadir):
        for file in files:
            filepath= os.path.join(root, file)
            if os.path.isfile(filepath):
                if file.lower().endswith("pdf"):
                    ## Trata arquivos PDF
                    ext = 'pdf'
                    loader=PyPDFLoader(filepath)
                    loaded_doc = loader.load()
                    ## Adição de metadados
                    for d in loaded_doc:
                        d.metadata.update({
                            "source": filepath,
                            "filename": os.path.basename(filepath),
                            "filetype": ext,
                            "doc_id": generate_doc_id(filepath),
                            "ingest_date": datetime.now().isoformat()
                    })
                    ## Gera lista com os documentos carregados
                    docs.extend(loaded_doc)
                    print(f"Arquivo {file} carregado")
    return docs
    
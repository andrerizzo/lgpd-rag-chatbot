
import hashlib

def generate_doc_id(filepath):
    """
    Gera um identificador único para um documento com base no caminho do arquivo.

    Utiliza o algoritmo SHA-1 para criar um hash do caminho do arquivo (filepath),
    garantindo a criação de um ID exclusivo e reprodutível para cada documento.

    Parameters:
        filepath (str): Caminho completo do arquivo.

    Returns:
        str: Hash SHA-1 em formato hexadecimal representando o ID único do documento.
    """
    return hashlib.sha1(filepath.encode()).hexdigest()
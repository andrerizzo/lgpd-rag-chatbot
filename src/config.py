
import os
from dotenv import load_dotenv

"""
Arquivo de configuração global do projeto RAG.

Este módulo define parâmetros centrais usados em múltiplos componentes do sistema,
como o nome dos modelos de linguagem, caminhos de dados, diretório do banco vetorial,
e tamanhos de chunking. Variáveis sensíveis como chaves de API são carregadas via .env.

A alteração deste arquivo afeta diretamente o comportamento do pipeline de ingestão,
embedding e resposta via LLM.

Variáveis principais:
- OPENAI_API_KEY
- LLM_MODEL
- EMBEDDING_MODEL
- DB_NAME
- DATA_DIR
- CHUNK_SIZE
- CHUNK_OVERLAP
"""

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
LLM_MODEL = "gpt-4o-mini"
EMBEDDING_MODEL = "text-embedding-3-small"
DB_NAME = "vector_db"
DATA_DIR = "data"
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 50
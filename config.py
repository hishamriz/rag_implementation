import os #enviroment variables
from pathlib import Path # pathlb module OOP style handling of filesystem paths

# Project root directory
ROOT_DIR = Path(__file__).parent

# Database configuration
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': int(os.getenv('DB_PORT', 5432)),
    'database': os.getenv('DB_NAME', 'rag_knowledge_base'),
    'user': os.getenv('DB_USER', 'postgres'),
    'password': os.getenv('DB_PASSWORD', '')
}

# Model configuration
MODEL_CONFIG = {
    'embedding_model': 'sentence-transformers/all-mpnet-base-v2',
    'generator_model': 'gpt-3.5-turbo',
    'embedding_cache_path': ROOT_DIR / 'knowledge_base/embeddings.pkl',
    'batch_size': 32
}

# Retriever configuration
RETRIEVER_CONFIG = {
    'max_results': 5,
    'similarity_threshold': 0.7,
    'use_hybrid_search': True
}

# API configuration
API_CONFIG = {
    'openai_api_key': os.getenv('OPENAI_API_KEY'),
}

# Paths configuration
PATHS = {
    'documents': ROOT_DIR / 'knowledge_base/documents',
    'sample_claims': ROOT_DIR / 'data/sample_claims',
    'competitor_analysis': ROOT_DIR / 'data/competitor_analysis'
}

# Ensure all directories exist
for path in PATHS.values():
    path.mkdir(parents=True, exist_ok=True)
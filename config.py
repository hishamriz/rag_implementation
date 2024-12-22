import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Project root directory
ROOT_DIR = Path(__file__).parent

# Database configuration
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': int(os.getenv('DB_PORT', 5432)),
    'database': os.getenv('DB_NAME', 'rag_knowledge_base'),
    'user': os.getenv('DB_USER', 'postgres'),
    'password': os.getenv('DB_PASSWORD', '')  # This will now come from .env file
}

# Rest of your config remains the same...
# Rest of your config remains the same...
API_CONFIG = {
    'openai_api_key': os.getenv('OPENAI_API_KEY'),  # Fetches the API key from the environment variable
}

import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PG_HOST = os.getenv("PG_HOST", "localhost")
PG_PORT = os.getenv("PG_PORT", "5432")
PG_DB = os.getenv("PG_DB", "seubanco")
PG_USER = os.getenv("PG_USER", "seuusuario")
PG_PASS = os.getenv("PG_PASS", "suasenha")

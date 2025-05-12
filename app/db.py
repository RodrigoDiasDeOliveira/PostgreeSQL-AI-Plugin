import psycopg2
from app.config import PG_DB, PG_USER, PG_PASS, PG_HOST, PG_PORT

def get_connection():
    return psycopg2.connect(
        dbname=PG_DB,
        user=PG_USER,
        password=PG_PASS,
        host=PG_HOST,
        port=PG_PORT
    )

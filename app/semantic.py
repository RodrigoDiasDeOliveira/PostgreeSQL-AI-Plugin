import openai
import numpy as np
import psycopg2
from pgvector.psycopg2 import register_vector

# Conecta-se ao banco e registra extensão vetorial
def get_pg_connection():
    conn = psycopg2.connect(
        dbname="sua_base",
        user="seu_usuario",
        password="sua_senha",
        host="localhost",
        port=5432
    )
    register_vector(conn)
    return conn

# Gera embedding com OpenAI
def generate_embedding(text: str) -> list:
    response = openai.Embedding.create(
        input=text,
        model="text-embedding-ada-002"
    )
    return response["data"][0]["embedding"]

# Insere embedding no banco
def store_embedding(text: str, metadata: dict):
    conn = get_pg_connection()
    cur = conn.cursor()

    embedding = generate_embedding(text)

    cur.execute(
        "INSERT INTO documents (content, embedding, metadata) VALUES (%s, %s, %s)",
        (text, embedding, metadata)
    )

    conn.commit()
    cur.close()
    conn.close()

# Busca por similaridade vetorial
def semantic_search(query: str, top_k: int = 5):
    conn = get_pg_connection()
    cur = conn.cursor()

    query_embedding = generate_embedding(query)

    cur.execute(
        """
        SELECT content, metadata
        FROM documents
        ORDER BY embedding <-> %s
        LIMIT %s
        """,
        (query_embedding, top_k)
    )

    results = cur.fetchall()
    cur.close()
    conn.close()

    return results

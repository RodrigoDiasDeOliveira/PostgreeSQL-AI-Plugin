from fastapi import FastAPI
from pydantic import BaseModel
from app.embedding import get_embedding
from app.db import get_connection

app = FastAPI()

class QueryRequest(BaseModel):
    user_query: str

@app.post("/semantic-search/")
def semantic_search(request: QueryRequest):
    embedding = get_embedding(request.user_query)
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT texto, embedding <-> %s AS distancia
        FROM documentos
        ORDER BY distancia ASC
        LIMIT 5;
    """, (embedding.tolist(),))
    resultados = cur.fetchall()
    cur.close()
    conn.close()
    return {"resultados": resultados}

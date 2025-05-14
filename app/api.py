from fastapi import FastAPI, Query
from pydantic import BaseModel
from embeddings import get_embedding
from semantics import semantic_search
from generative_assistant import suggest_improvements, analyze_embedding_use

app = FastAPI(title="Vector AI Plugin for PostgreSQL")

class TextInput(BaseModel):
    text: str

class SearchInput(BaseModel):
    query: str
    top_k: int = 5

@app.post("/embed")
def generate_embedding(input: TextInput):
    embedding = get_embedding(input.text)
    return {"embedding": embedding}

@app.post("/semantic_search")
def search_semantics(input: SearchInput):
    results = semantic_search(input.query, input.top_k)
    return {"results": results}

@app.post("/suggest")
def suggest_query_improvements(input: TextInput):
    suggestion = suggest_improvements(input.text)
    return {"suggestion": suggestion}

@app.post("/analyze_embedding_use")
def analyze_embedding_feedback(input: TextInput):
    analysis = analyze_embedding_use(input.text)
    return {"analysis": analysis}

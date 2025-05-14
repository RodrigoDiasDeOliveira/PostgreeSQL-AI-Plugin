from transformers import pipeline

# Carrega o pipeline de texto para texto (pode ajustar o modelo)
qa_pipeline = pipeline("text2text-generation", model="google/flan-t5-base")

def suggest_improvements(query: str) -> str:
    prompt = f"Suggest optimizations or improvements for the following SQL or natural language query:\n{query}"
    result = qa_pipeline(prompt, max_new_tokens=100)
    return result[0]["generated_text"]

def analyze_embedding_use(text: str) -> str:
    prompt = f"Analyze the effectiveness and clarity of using embeddings in this context:\n{text}"
    result = qa_pipeline(prompt, max_new_tokens=100)
    return result[0]["generated_text"]


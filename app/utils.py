import json
import logging
import os
from dotenv import load_dotenv
from typing import Union

# Carrega variáveis de ambiente do .env
load_dotenv()

# Configura logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("vector_ai_plugin")

# Função para carregar configurações do ambiente
def get_env_var(key: str, default: Union[str, None] = None) -> str:
    value = os.getenv(key, default)
    if value is None:
        logger.warning(f"Variável de ambiente {key} não encontrada.")
    return value

# Formata resposta JSON padrão
def format_response(status: str, data: Union[str, dict, list]) -> dict:
    return {
        "status": status,
        "data": data
    }

# Serializa JSON para uso em logs ou respostas
def to_pretty_json(data: Union[dict, list]) -> str:
    return json.dumps(data, indent=2, ensure_ascii=False)

# Validação simples de entrada
def is_valid_text(text: str) -> bool:
    return bool(text and isinstance(text, str) and len(text.strip()) > 3)

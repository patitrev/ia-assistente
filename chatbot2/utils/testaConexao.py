from dotenv import load_dotenv
import openai
import os

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Obter a chave da API da variável de ambiente
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")

# Configurar a chave da API
openai.api_key = api_key

# Testar a conexão
try:
    response = openai.Model.list()
    print("API Key is valid. Available models:", response)
except Exception as e:
    print("An error occurred:", e)

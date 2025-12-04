from agno.knowledge.embedder.google import GeminiEmbedder
from dotenv import load_dotenv
import os

load_dotenv()

print("API KEY encontrada?", "SIM" if os.getenv("GOOGLE_API_KEY") else "NÃO")

try:
    embedder = GeminiEmbedder(id="models/text-embedding-004")

    print("\nGerando embedding com get_embedding...")

    # um texto simples de teste
    vetor = embedder.get_embedding("teste de embedding")

    print("\nEmbedding gerado com sucesso!\n")
    print("Tipo do objeto:", type(vetor))
    print("Tamanho do vetor:", len(vetor))
    print("Primeiros 10 valores:", vetor[:10])

except Exception as e:
    print("\n❌ ERRO AO GERAR EMBEDDING ❌\n")
    print(repr(e))

import os
# Importa as funções do seu arquivo ingestao.py
from alimentacao import criar_banco_vetorial, realizar_alimentacao

def rodar_teste():
    # --- 1. Setup (Cria dados falsos para teste) ---
    print("--- SETUP DE TESTE ---")

    pasta_pdfs = "data/jardinagem_construcao_alimentos_servicos"
    nome_db = "db_casa"
    db = criar_banco_vetorial(nome_db)
    
    # --- 3. Testando a Ingestão ---
    print("Iniciando ingestão...")
    # Note que passamos o 'db' que criamos acima
    kb = realizar_alimentacao(pasta_pdfs, db)


if __name__ == "__main__":
    rodar_teste()
import os
# Importa as funções do seu arquivo ingestao.py
from alimentacao import criar_banco_vetorial, realizar_alimentacao

def rodar_teste():
    # --- 1. Setup (Cria dados falsos para teste) ---
    print("--- SETUP DE TESTE ---")
    pasta_teste = "./temp_pdfs"
    csv_teste = "./temp_dados.csv"
    nome_banco = "banco_agente_financeiro" # Testando a separação por agente
    
    if not os.path.exists(pasta_teste): os.makedirs(pasta_teste)
    
    # Criar um CSV dummy
    with open(csv_teste, "w") as f:
        f.write("produto,preco,detalhe\nLaptop,5000,Processador rapido")
    
    # --- 2. Testando a Criação do Banco ---
    print(f"\nCriando banco para o agente: {nome_banco}...")
    db = criar_banco_vetorial(nome_banco)
    
    # --- 3. Testando a Ingestão ---
    print("Iniciando ingestão...")
    # Note que passamos o 'db' que criamos acima
    kb = realizar_alimentacao(pasta_teste, csv_teste, db)
    
    # --- 4. A Prova Real (Busca) ---
    # Se isso funcionar, seu código está perfeito.
    print("\n--- TESTE DE BUSCA ---")
    try:
        # Tenta buscar algo que escrevemos no CSV
        resultados = kb.search(query="Processador rapido", num_documents=1)
        if resultados:
            print(f"🎉 SUCESSO! Encontrado: {resultados[0].content}")
        else:
            print("⚠️ Ingestão rodou, mas busca falhou (talvez CSV vazio?).")
    except Exception as e:
        print(f"❌ Erro na busca: {e}")

    # Limpeza (Opcional - remove os arquivos de teste)
    # os.remove(csv_teste)
    # os.rmdir(pasta_teste)

if __name__ == "__main__":
    rodar_teste()
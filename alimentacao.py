import os # ajuda a encontrar as pastas corretamente, mesmo em sistemas operacionais diferentes 
from agno.knowledge import Knowledge
from agno.knowledge.reader.pdf_reader import PDFReader
from agno.knowledge.reader.csv_reader import CSVReader
from agno.vectordb.lancedb import LanceDb, SearchType
from agno.knowledge.embedder.google import GeminiEmbedder

# Configurando onde o banco vetorial ficará salvo

def criar_banco_vetorial(nome_banco_vetorial):

    # para as bibliotecas utilizarem o Gemini em vez do padrão, que é a OpenAI
    embedder_google = GeminiEmbedder( 
        api_key=os.getenv("GOOGLE_API_KEY"),
        id="models/embedding-001",
    )

    db = LanceDb(
        table_name = nome_banco_vetorial, 
        uri = f"./{nome_banco_vetorial}", # pasta será criada aqui
        search_type = SearchType.hybrid, # Busca híbrida (tanto por palavras-chave, quanto por semântica)
        embedder=embedder_google
    )

    return db

def realizar_alimentacao(path_pasta, path_pagina_planilha, db):

    if not os.path.exists(path_pasta):
        print(f"O caminho para a pasta {path_pasta} é inválido.")
        return # para sair da função caso dê esse erro

    elif not os.path.exists(path_pagina_planilha):
        print(f"O caminho para a página da planilha {path_pagina_planilha} é inválido.")
        return 
    
    # se chegar a essa linha, é porque encontrou os dois caminhos 
    
    pdf_knowledge = Knowledge( # tiramos as declarações dos leitores de dentro de pdf_knowledge e csv_knowledge porque os leitores são declarados depois, dentro de add_contents
        vector_db = db
    )

    csv_knowledge = Knowledge(
        vector_db = db
    )

    print("Recolhendo as informações dos PDFs...")

    pdf_knowledge.add_contents(
    PDFReader(chunk=True).read(path=path_pasta)
    )

    print("Recolhendo as informações da planilha...")

    csv_knowledge.add_contents(
    CSVReader(chunk=True).read(path=path_pagina_planilha)
    )
    
    print("Alimentação bem-sucedida!")

# --- Bloco de Execução Direta (Corrigido) ---
if __name__ == "__main__":
    # 1. Defina caminhos reais ou de teste aqui
    pasta = "./meus_pdfs" # Garanta que essa pasta existe
    planilha = "./dados.csv" # Garanta que esse arquivo existe
    nome_do_banco = "banco_teste_main"

    # 2. Cria o objeto do banco PRIMEIRO
    meu_banco = criar_banco_vetorial(nome_do_banco)

    # 3. Chama a função passando os 3 argumentos
    realizar_alimentacao(pasta, planilha, meu_banco)

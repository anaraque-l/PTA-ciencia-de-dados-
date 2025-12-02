import os # ajuda a encontrar as pastas corretamente, mesmo em sistemas operacionais diferentes 
from agno.knowledge import Knowledge
from agno.knowledge.reader.pdf_reader import PDFReader
from agno.vectordb.lancedb import LanceDb, SearchType
from agno.knowledge.embedder.google import GeminiEmbedder
from pathlib import Path

from dotenv import load_dotenv # Você precisará instalar: pip install python-dotenv

load_dotenv() # Isso carrega o arquivo .env para o sistema

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

def realizar_alimentacao(path_pasta, db):

    if not os.path.exists(path_pasta):
        print(f"O caminho para a pasta {path_pasta} é inválido.")
        return # para sair da função caso dê esse erro
    
    # se chegar a essa linha, é porque encontrou o caminho da pasta com os PDFs
    
    pdf_knowledge = Knowledge( # tiramos as declarações dos leitores de dentro de pdf_knowledge porque os leitores são declarados depois, dentro de add_contents
        vector_db = db
    )

    print("Recolhendo as informações dos PDFs...")

    pdfs = []

    path_pasta = Path(path_pasta)

    for arquivo_pdf in path_pasta.glob("*.pdf"):
        print(f"Lendo: {arquivo_pdf.name}")
        pdfs_arquivo = PDFReader(chunk=True).read(pdf=arquivo_pdf)
        pdfs.extend(pdfs_arquivo)

    if pdfs:
        print(f"Inserindo {len(pdfs)} fragmentos no banco...")
        pdf_knowledge.vector_db.insert(documents=pdfs, content_hash="carga_manual_pdfs")
        print("Ingestão concluída!")
    else:
        print("Nenhum PDF encontrado ou lido.")

    return pdf_knowledge
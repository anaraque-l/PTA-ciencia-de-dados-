import os
from pathlib import Path
from dotenv import load_dotenv

from agno.knowledge.agent import AgentKnowledge
from agno.document import Document
from agno.document.reader.pdf_reader import PDFReader
from agno.vectordb.chroma import ChromaDb
from agno.embedder.google import GeminiEmbedder

load_dotenv()


def criar_banco_vetorial(nome_banco_vetorial: str, area: str) -> ChromaDb:
    """
    Cria um banco vetorial Chroma usando GeminiEmbedder.
    Compatível com Agno 2.3.4.
    """

    db = ChromaDb(
        path=f"chromadb_storage/{area}_rag",
        collection=nome_banco_vetorial,
        persistent_client=True,
        embedder=GeminiEmbedder(id="models/text-embedding-004"),
    )

    return db


def realizar_alimentacao(path_pasta: str, db: ChromaDb) -> None:
    """
    Lê PDFs usando PDFPlumberReader (novo na versão 2.x),
    gera Document chunks e insere no ChromaDb via AgentKnowledge.
    """

    if not os.path.exists(path_pasta):
        print(f"❌ Caminho inválido: {path_pasta}")
        return
    
    path_pasta = Path(path_pasta)

    # knowledge = casca necessária para inserir no banco
    knowledge = AgentKnowledge(vector_db=db)

    print("📄 Lendo PDFs da pasta...")

    documentos: list[Document] = []

    reader = PDFReader(chunk=True)  # substitui PDFReader

    for pdf_file in path_pasta.glob("*.pdf"):
        if not pdf_file.is_file():
            continue

        print(f"➡️ Lendo: {pdf_file.name}")

        chunks = reader.read(pdf_file)
        documentos.extend(chunks)

    if not documentos:
        print("⚠️ Nenhum PDF encontrado ou lido.")
        return

    print(f"📥 Inserindo {len(documentos)} chunks no banco vetorial...")

    knowledge.load_documents(documents=documentos)

    print("✅ Ingestão concluída!")

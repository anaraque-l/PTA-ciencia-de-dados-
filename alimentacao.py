# Importações corretas para a versão atual da Agno
from agno.knowledge.pdf import PDFKnowledgeBase, PDFReader
from agno.knowledge.csv import CSVKnowledgeBase
from agno.knowledge.combined import CombinedKnowledgeBase
from agno.vectordb.lancedb import LanceDb, SearchType

# Configurando onde o banco vetorial ficará salvo
db_vetorial = LanceDb(
    nome = "base_vetorial",
    uri = "./dbvetorial", # pasta será criada aqui
    search_type = SearchType.hybrid # Busca híbrida (tanto por palavras-chave, quanto por semântica)
)

pdf_knowledge = PDFKnowledgeBase( # ajustar o nome
    path = "data/", # colocar o caminho para o pdf
    vector_db = db_vetorial,
    reader = PDFReader(chunk=True) # para realizar o chunking (quebra de texto em pedaços menores, mas ainda com semântica completa
)

csv_knowledge = CSVKnowledgeBase(
    path = "", # caminho da planilha
    vector_db = db_vetorial
)

def realizar_alimentacao():

    # TO DO terminar de adequar essa função às especificações do projeto (separação por categorias, iteração sobre os pdfs, etc)

    print("Recolhendo as informações dos PDFs...")
    pdf_knowledge.load(recreate=True) # recreate=True zera o banco de dados e recria-o

    print("Recolhendo as informações da planilha...")
    csv_knowledge.load(recreate=False) # recreate=False para não criar uma do zero, apenas adicionar

    print("Alimentação bem-sucedida!")

if __name__ == "__main__":
    realizar_alimentacao()


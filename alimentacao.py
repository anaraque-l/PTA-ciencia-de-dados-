from agno.knowledge.pdf import PDFKnowledgeBase, PDFReader
from agno.knowledge.csv import CSVKnowledgeBase
from agno.knowledge.combined import CombinedKnowledgeBase
from agno.vectordb.lancedb import LanceDb, SearchType

# Configurando onde o banco vetorial ficará salvo
db_vetorial = LanceDb(
    name = "base_vetorial",
    uri = "./dbvetorial", # pasta será criada aqui
    search_type = SearchType.hybrid # Busca híbrida (tanto por palavras-chave, quanto por semântica)
)

def realizar_alimentacao(path_pasta, path_pagina_planilha):

    pdf_knowledge = PDFKnowledgeBase( 
    path = path_pasta, 
    vector_db = db_vetorial,
    reader = PDFReader(chunk=True) # para realizar o chunking (quebra de texto em pedaços menores, mas ainda com semântica completa
    )

    csv_knowledge = CSVKnowledgeBase(
    path = path_pagina_planilha, 
    vector_db = db_vetorial
    )

    print("Recolhendo as informações dos PDFs...")
    pdf_knowledge.load(recreate=True) # recreate=True zera o banco de dados e recria-o

    print("Recolhendo as informações da planilha...")
    csv_knowledge.load(recreate=False) # recreate=False para não criar uma do zero, apenas adicionar

    print("Alimentação bem-sucedida!")

'''
if __name__ == "__main__":
    realizar_alimentacao(path_pasta, path_pagina_planilha)
'''

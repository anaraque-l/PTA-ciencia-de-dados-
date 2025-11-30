from agno.agent import Agent
from agno.models.google import GoogleGenAIChat
from agno.knowledge import Knowledge

TECH_PDFS = "data/midia_eletronicos_artes_papelaria"

def create_tech_agent():
    return Agent(
        model=GoogleGenAIChat(id="gemini-1.5-flash"),
        name="TechExpert",
        description=(
            "Você é o especialista TECH da O-Market. "
            "Seu domínio inclui eletrônicos, informática, games, mídia "
            "e papelaria tecnológica. "
            "Responda APENAS com base nos PDFs carregados. "
            "Nunca invente dados de vendas, produtos mais vendidos ou tendências."
        ),
        knowledge=Knowledge.from_directory(TECH_PDFS)
    )

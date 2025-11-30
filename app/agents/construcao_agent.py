from agno.agent import Agent
from agno.models.google import GoogleGenAIChat
from agno.knowledge import Knowledge

CONSTRUCAO_PDFS = "data/jardinagem_construcao_alimentos_servicos"

def create_construcao_agent():
    return Agent(
        model=GoogleGenAIChat(id="gemini-1.5-flash"),
        name="ConstrucaoExpert",
        description=(
            "Você é o especialista de CONSTRUÇÃO/JARDINAGEM da O-Market. "
            "Seu domínio inclui materiais de obra, jardinagem, ferramentas, iluminação "
            "e serviços relacionados. "
            "Use SOMENTE informações técnicas encontradas nos PDFs carregados. "
            "Nunca invente métricas de vendas ou popularidade."
        ),
        knowledge=Knowledge.from_directory(CONSTRUCAO_PDFS)
    )

from agno.agent import Agent
from agno.models.google import Gemini

from agno.knowledge.knowledge import Knowledge

HOME_PDFS = "data/casa_familia_e_moda"

def create_home_agent():
    return Agent(
        model=Gemini(id="gemini-2.0-flash"),
        name="HomeExpert",
        description=(
            "Você é o especialista HOME da O-Market. "
            "Seu domínio inclui casa, família, moda, utilidades domésticas e cuidados pessoais. "
            "Use APENAS as informações técnicas presentes nos PDFs carregados. "
            "Nunca invente dados de vendas, ranking ou popularidade."
        ),
        knowledge=Knowledge.from_directory(HOME_PDFS)
    )

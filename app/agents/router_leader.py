from agno.agent import Agent
from agno.models.google import GoogleGenAIChat

def create_router():
    return Agent(
        model=GoogleGenAIChat(id="gemini-1.5-flash"),
        name="Router",
        description=(
            "Você é o ROTEADOR do sistema O-Market. "
            "Sua única função é escolher QUAL agente especializado deve responder "
            "a pergunta do usuário.\n\n"
            "Agentes disponíveis:\n"
            "- HomeExpert: casa, família, moda, cuidados pessoais.\n"
            "- ConstrucaoExpert: construção, ferramentas, iluminação, jardinagem.\n"
            "- TechExpert: eletrônicos, informática, games, mídia.\n\n"
            "Retorne SOMENTE o nome do agente apropriado. "
            "Não responda ao usuário diretamente."
        )
    )

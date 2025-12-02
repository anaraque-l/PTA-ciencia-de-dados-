from agno.agent import Agent
from agno.models.google import GoogleGenAIChat
from agno.knowledge import Knowledge

from app.tools.ler_csv_itens_pedidos import buscar_itens_pedidos_por_id
from app.tools.ler_csv_produtos import buscar_produto_por_id
from app.tools.ler_csv_pedidos import buscar_pedido_por_id
from app.tools.ler_csv_vendedores import buscar_vendedores_por_id

HOME_PDFS = "data/casa_familia_e_moda"

def create_home_agent():
    return Agent(
        model=GoogleGenAIChat(id="gemini-1.5-flash"),
        name="HomeExpert",
        description=(
            "Você é o especialista HOME da O-Market. "
            "Seu domínio inclui casa, família, moda, utilidades domésticas e cuidados pessoais. "
            "Use APENAS as informações técnicas presentes nos PDFs carregados, e quando a informação solicitada"
            "envolver pedidos, produtos, itens pedidos ou vendedores, use as ferramentas"
            "Nunca invente dados de vendas, ranking ou popularidade."
        ),
        knowledge=Knowledge.from_directory(HOME_PDFS),
        tools=[buscar_itens_pedidos_por_id, buscar_produto_por_id, buscar_pedido_por_id, buscar_vendedores_por_id]
    )

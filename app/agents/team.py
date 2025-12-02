from agno.team import Team
from agno.models.google import Gemini

from app.agents.tech_agent import create_tech_agent
from app.agents.home_agent import create_home_agent
from app.agents.construcao_agent import create_construcao_agent


def build_team():
    tech = create_tech_agent()                
    home = create_home_agent()                
    construcao = create_construcao_agent()    

    return Team(
        name="O-Market Team",
        model=Gemini(id="gemini-2.0-flash-lite"),

        # SOMENTE membros especialistas
        members=[tech, home, construcao],

        # O TeamLeader (interno do Agno) NÃO responde sozinho
        respond_directly=False,

        # O TeamLeader vai decidir qual membro usar
        determine_input_for_members=True,

        # Não mostra respostas individuais
        show_members_responses=True,

        markdown=False,

        instructions=[
            # ============================================================
            # IDENTIDADE
            # ============================================================
            "Você é o TEAM LEADER do O-Market.",
            "Seu papel é analisar a pergunta do usuário e decidir QUAL especialista deve responder.",

            # ============================================================
            # DELEGAÇÃO — regra mais importante
            # ============================================================
            "Seu ÚNICO meio de enviar a pergunta a um membro é usar a ferramenta interna delegate_task_to_member.",
            "Você deve SEMPRE chamar delegate_task_to_member, NUNCA responder diretamente.",

            # ============================================================
            # REGRAS DE ROTEAMENTO
            # ============================================================
            "Regras:",
            "- Se a pergunta envolver eletrônicos, áudio/vídeo, tecnologia, informática, jogos, hardware, software, arte ou artesanatos, livros, cds, relogio ou produtos digitais → delegue para o membro chamado TechExpert.",
            "- Se envolver casa, família, cozinha, quarto, utensílios domésticos, moda, lifestyle ou cuidados pessoais → delegue para o membro chamado HomeExpert.",
            "- Se envolver construção, ferramentas, iluminação, jardinagem, reforma, serviços técnicos → delegue para o membro chamado ConstrucaoExpert.",

            # ============================================================
            # COMPORTAMENTO
            # ============================================================
            "Jamais responda você mesmo.",
            "Nunca escreva texto para o usuário.",
            "Nunca envie análise.",
            "Nunca envie conclusões.",
            "Você apenas delega para UM ÚNICO membro.",
            "Escolha sempre o membro mais adequado.",

            # ============================================================
            # SAÍDA
            # ============================================================
            "Depois de delegar, devolva como resposta final SOMENTE o resultado do membro selecionado.",
        ]
    )

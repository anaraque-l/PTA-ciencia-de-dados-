from agno.os import AgentOS  
from agno.agent import Agent  

from app.agents.casa import create_home_agent  # seu agente já configurado

agent = create_home_agent()

agent_os = AgentOS(
    agents=[agent],
    # você pode passar mais agentes, equipes ou workflows se tiver
)

app = agent_os.get_app()

if __name__ == "__main__":
    agent_os.serve(app="agentos:app", reload=True)

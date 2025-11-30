from agno.team import Team

from app.agents.home_agent import create_home_agent
from app.agents.construcao_agent import create_construcao_agent
from app.agents.tech_agent import create_tech_agent
from app.agents.router_leader import create_router


def build_team():
    router = create_router()
    home = create_home_agent()
    const = create_construcao_agent()
    tech = create_tech_agent()

    return Team(
        leader=router,
        agents=[home, const, tech],
        mode="route"
    )
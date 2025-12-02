from agno.run import RunConfig
from app.agents.team import build_team

team = build_team()

def route(query: str):
    return team.run_sync(
        query,
        run_config=RunConfig(
            reasoning=True,
            search_knowledge=True,
            reflexion=True
        )
    )


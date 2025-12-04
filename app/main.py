from fastapi import FastAPI
from pydantic import BaseModel
from app.agents.team import build_team

# Carrega o time de agentes (ele mesmo fará o roteamento)
agent = build_team()

app = FastAPI(
    title="Agno Agents API",
    description="API compatível com o Agno Cloud Playground",
    version="1.0.0"
)

class PlaygroundRequest(BaseModel):
    input: str

class PlaygroundResponse(BaseModel):
    output: str
   

@app.post("/v1", response_model=PlaygroundResponse)
def run_agent(request: PlaygroundRequest):
    resultado = agent.run(request.input)

    # Para Team() → a resposta está SEMPRE aqui:
    resposta = resultado.content


    return PlaygroundResponse(
        output=resposta,
        
    )

@app.get("/")
def root():
    return {
        "message": "API Agno ativa",
        "playground_url": "https://app.agno.com/playground?endpoint=http://localhost:7777"
    }

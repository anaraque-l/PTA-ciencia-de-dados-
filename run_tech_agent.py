from app.agents.tech_agent import create_tech_agent

agent = create_tech_agent()

while True:
    pergunta = input("\nVocê: ")
    resposta = agent.run(pergunta)
    print("\nTechExpert:", resposta.content)

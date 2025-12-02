from app.agents.home_agent import create_home_agent 

agent = create_home_agent()

print("\n=== HomeExpert da O-Market ===")
print("Digite sua pergunta (ou 'exit' para sair).")
print("-------------------------------------------")

while True:
    pergunta = input("\nVocê: ")

    if pergunta.lower() in ["exit", "sair", "quit"]:
        print("Encerrando...")
        break

    resposta = agent.run(pergunta)
    print("\nHomeExpert:", resposta.content)

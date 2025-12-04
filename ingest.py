from app.alimentacao import criar_banco_vetorial, realizar_alimentacao

# TECH
db_tech = criar_banco_vetorial("tech_rag", "tech")
knowledge_tech = realizar_alimentacao("data/midia_eletronicos_artes_papelaria", db_tech)

# HOME
db_home = criar_banco_vetorial("home_rag", "home")
knowledge_home = realizar_alimentacao("data/casa_familia_e_moda", db_home)

# CONSTRUÇÃO
db_construcao = criar_banco_vetorial("construcao_rag", "construcao")
knowledge_construcao = realizar_alimentacao("data/jardinagem_construcao_alimentos_servicos", db_construcao)


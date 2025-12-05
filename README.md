# 🧠 O-MARKET — Sistema Multiagente de Ciência de Dados

Este projeto implementa um **Sistema Multiagente com Agno** para responder perguntas técnicas sobre produtos da O-Market, utilizando **PDFs vetorizados como única fonte de verdade**.

---

## 🎯 Objetivo

Criar um ambiente em que qualquer usuário consiga perguntar:

> “Esse produto tem suporte VESA?”

E o sistema responda:

> “TechExpert: Sim, conforme catálogo, o modelo X aceita suporte VESA 75×75 e 100×100.  
> **Fontes:** catalogo_monitores.pdf”

---

## 🛠 Tecnologias Utilizadas

| Componente | Tecnologia |
|---|---|
| Linguagem | Python |
| Multiagentes | Agno |
| Modelo | Gemini 2.5-flash |
| Embeddings | text-embedding-004 |
| Vetor DB | ChromaDB |
| Leitura de PDFs | PDFReader (chunk) |
| Playground | Agno Cloud |
| Ambiente | VSCode + venv |

---

## 📚 Fontes de Conhecimento

Todos os dados vêm **exclusivamente dos PDFs** organizados em pastas:

data/
midia_eletronicos_artes_papelaria/
casa_familia_moda/
jardinagem_construcao_servicos/

css
Copy code

Cada PDF é lido com:

```python
reader = PDFReader(chunk=True)
chunks = reader.read(pdf_file)
Os chunks são enviados para o vetor DB:

python
Copy code
knowledge.load_documents(documents=chunks)
🧬 Arquitetura
sql
Copy code
+-------------------+
|    Usuário Final  |
+---------+---------+
          |
          v
+---------+---------+
|   Playground UI   |
+---------+---------+
          |
          v
+---------+---------+
|   Router Agent    |
| (decide domínio)  |
+---+-----------+---+
    |           |
    |           +--------------------+
    |                                |
    v                                v
+----------+                 +--------------+
| TechExp. |                 | HomeExpert   |
+----------+                 +--------------+
    |
    v
+--------------------------------+
| ConstrucaoExpert               |
+--------------------------------+
Cada agente responde apenas se a pergunta pertence ao seu domínio.

🤖 Agentes Criados
Agente	Domínio
TechExpert	tecnologia, eletrônicos, áudio, PCs
HomeExpert	casa, família, moda, beleza, pet
ConstrucaoExpert	construção, jardinagem, serviços, alimentos

📐 Regras de Domínio
Cada agente possui regras rígidas.

Quando a pergunta é do domínio:
makefile
Copy code
TechExpert:
<resposta>
Quando não é do domínio:
css
Copy code
Este tema pertence a outro agente.
🧠 Roteador
O Roteador NUNCA responde ao usuário diretamente.

Formato obrigatório:

vbnet
Copy code
<delegate to="TechExpert">
ou

vbnet
Copy code
<delegate to="HomeExpert">
ou

vbnet
Copy code
<delegate to="ConstrucaoExpert">
Se não reconhecer, encaminha para TechExpert.

📌 Regras de Resposta dos Agentes
Cada resposta deve:

✔ Começar com o nome do agente:

makefile
Copy code
TechExpert:
HomeExpert:
ConstrucaoExpert:
✔ Usar somente dados dos PDFs

✔ Citar fontes no final:

makefile
Copy code
Fontes: nome1.pdf, nome2.pdf
✔ Se não houver dados suficientes:

powershell
Copy code
Não há dados suficientes nos PDFs para responder.
🗂 Banco Vetorial
O armazenamento é persistente via ChromaDB.

Pasta:

Copy code
chromadb_storage/
Coleções:

tech_rag

home_rag

construcao_rag

Embedder utilizado:

bash
Copy code
GeminiEmbedder(id="text-embedding-004")
📁 Estrutura do Projeto
css
Copy code
app/
  agents/
    tech_agent.py
    home_agent.py
    construcao_agent.py
    team.py
  alimentacao.py
  main.py

data/
  midia_eletronicos_artes_papelaria/
  casa_familia_moda/
  jardinagem_construcao_servicos/

chromadb_storage/
venv/
README.md
🚀 Execução
1. Alimentação dos Bancos Vetoriais
python
Copy code
from app.alimentacao import criar_banco_vetorial, realizar_alimentacao

db = criar_banco_vetorial("tech_rag", "tech")
realizar_alimentacao("data/midia_eletronicos_artes_papelaria", db)
Repetir para:

home_rag com pasta casa_familia_moda

construcao_rag com pasta jardinagem_construcao_servicos

2. Rodar API
bash
Copy code
uvicorn app.main:app --reload
3. Abrir Playground
Acessar:

bash
Copy code
https://app.agno.com/playground?endpoint=http://localhost:7777
🧪 Testes Realizados
✔ Perguntas sobre especificações técnicas
✔ Citações corretas dos PDFs
✔ Nenhuma invenção
✔ Roteamento fiel
✔ Respostas padronizadas

Exemplo real
Pergunta:

nginx
Copy code
Esse monitor tem VESA?
Resposta:

makefile
Copy code
TechExpert: Sim, o modelo X possui padrões VESA 75x75 e 100x100.
Fontes: catalogo_monitores.pdf
Outro exemplo
Pergunta:

nginx
Copy code
Essa roupa infantil aparece nos PDFs?
Resposta:

makefile
Copy code
HomeExpert: Sim, há PDF contendo catálogo de roupas infanto-juvenis.
Fontes: fashion_roupa_infanto_juvenil.pdf
Se a pergunta não pertence ao agente:

css
Copy code
Este tema pertence a outro agente.
Se não há dados:

powershell
Copy code
Não há dados suficientes nos PDFs para responder.
🎉 Resultado Final
O sistema entrega:

✔ Arquitetura multiagente robusta
✔ Roteador com delegação automática
✔ Três agentes especialistas independentes
✔ Respostas técnicas baseadas em PDFs
✔ Reconhecimento de domínio
✔ Nenhuma invenção
✔ Modelo utilizado: Gemini 2.5-flash

🏁 Conclusão
Este projeto demonstra um pipeline completo de:

ingestão de PDFs

criação de banco vetorial

construção de agentes especialistas

roteamento automático

interface via Playground Agno

Permitindo que qualquer pessoa faça perguntas em linguagem natural sobre produtos — com respostas fidedignas, técnicas e verificáveis.


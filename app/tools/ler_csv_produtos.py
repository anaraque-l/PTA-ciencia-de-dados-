from agno.tools import tool
import csv
from typing import Optional, Dict

CSV_FILE_PATH = "data/produtos.csv"

@tool
def buscar_produto_por_id(id_produto: str) -> Optional[Dict]:
    """
    Busca no CSV (streaming) o produto com o id_produto fornecido.
    Não carrega o CSV inteiro na memória.

    Args:
    id_produto(str)

    return:
    dados do produto em questão (dict)
    """
    try:
        with open(CSV_FILE_PATH, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                if row.get("id_produto", "").strip().lower() == id_produto.strip().lower():
                    return row
            
        return None

    except Exception as e:
        return {"erro": str(e)}

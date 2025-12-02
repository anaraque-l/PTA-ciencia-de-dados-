from agno.tools import tool
import csv
from typing import Optional, Dict

CSV_FILE_PATH = "data/itens_pedidos.csv"

@tool
def buscar_itens_pedidos_por_id(id_itens_pedidos: str) -> Optional[Dict]:
    """
    Busca no CSV (streaming) os itens pedidos com o id_itens_pedidos fornecido.
    Não carrega o CSV inteiro na memória.

    Args:
    id_itens_pedidos(str)

    return:
    dados dos itens pedidos em questão (dict)
    """
    try:
        with open(CSV_FILE_PATH, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                if row.get("id_itens_pedidos", "").strip().lower() == id_itens_pedidos.strip().lower():
                    return row
            
        return None

    except Exception as e:
        return {"erro": str(e)}

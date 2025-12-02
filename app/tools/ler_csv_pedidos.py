from agno.tools import tool
import csv
from typing import Optional, Dict

CSV_FILE_PATH = "data/pedidos.csv"

@tool
def buscar_pedido_por_id(id_pedido: str) -> Optional[Dict]:
    """
    Busca no CSV (streaming) o pedido com o id_pedido fornecido.
    Não carrega o CSV inteiro na memória.

    Args:
    id_pedido(str)

    return:
    dados do pedido em questão (dict)
    """
    try:
        with open(CSV_FILE_PATH, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                if row.get("id_pedido", "").strip().lower() == id_pedido.strip().lower():
                    return row
            
        return None

    except Exception as e:
        return {"erro": str(e)}

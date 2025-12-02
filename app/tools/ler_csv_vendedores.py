from agno.tools import tool
import csv
from typing import Optional, Dict

CSV_FILE_PATH = "data/vendedores.csv"

@tool
def buscar_vendedores_por_id(id_vendedor: str) -> Optional[Dict]:
    """
    Busca no CSV (streaming) o vendedor com o id_vendedor fornecido.
    Não carrega o CSV inteiro na memória.

    Args:
    id_vendedor(str)

    return:
    dados do vendedor em questão (dict)
    """
    try:
        with open(CSV_FILE_PATH, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                if row.get("id_vendedor", "").strip().lower() == id_vendedor.strip().lower():
                    return row
            
        return None

    except Exception as e:
        return {"erro": str(e)}

from pathlib import Path
from agno.storage.sqlite import SqliteStorage

def get_team_storage():
    path = Path("agno_storage")
    path.mkdir(exist_ok=True)

    return SqliteStorage(
        table_name="team_sessions",
        db_file=str(path / "team_sessions.db"),
        mode="team",
        auto_upgrade_schema=True
    )

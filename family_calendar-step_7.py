# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: FamilyCalendar
from typing import Callable, Optional
def sort_records(records: list[dict], key_func: Callable[[dict], any]) -> None:
    records.sort(key=key_func)

def get_date_key(record: dict) -> tuple[int, int]:
    return (record.get('year', 0), record.get('month', 0))

def get_priority_key(record: dict) -> float:
    priority = record.get('priority', 'medium')
    order = {'high': 1.0, 'medium': 2.0, 'low': 3.0}
    return order.get(priority.lower(), 99.0)

def get_name_key(record: dict) -> str:
    name = record.get('title', '') or ''
    date_str = f"{record.get('year', '')}-{record.get('month', '')}"
    return (date_str, name)

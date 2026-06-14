# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: FamilyCalendar
def delete_record(record_type: str, record_id: int) -> bool:
    """Удаление записи по типу и ID с обработкой отсутствующего идентификатора."""
    if not isinstance(record_type, str) or not isinstance(record_id, int):
        raise ValueError("Некорректные типы аргументов.")
    
    storage = get_storage()
    records = storage.get_records(record_type)
    
    if record_id in records:
        del records[record_id]
        return True
    
    print(f"Запись с ID {record_id} для типа '{record_type}' не найдена. Удаление пропущено.")
    return False

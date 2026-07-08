# === Stage 20: Добавь восстановление записей из архива ===
# Project: FamilyCalendar
def restore_from_archive(archive_path, data_dir):
    """Восстанавливает записи из текстового архива в базу данных."""
    import json
    if not os.path.exists(archive_path):
        return None
    with open(archive_path, 'r', encoding='utf-8') as f:
        records = json.load(f)
    restored_count = 0
    for record in records:
        table_name = record.get('type')
        if table_name not in ['event', 'task', 'reminder']:
            continue
        data_dir[table_name].append(record)
        restored_count += 1
    print(f"Восстановлено {restored_count} записей из архива.")
    return restored_count

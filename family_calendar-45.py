# === Stage 45: Добавь восстановление из резервной копии ===
# Project: FamilyCalendar
def load_from_backup(backup_path: str) -> None:
    """Восстанавливает данные из текстового резервного файла формата,
    созданного load_to_backup(). Формат:
    # FamilyCalendar Backup v1.0
    <дата>
    <количество записей>
    <тип_записи>:<id>:<имя>:<дата_начала>:<дата_конца>:<текст>
    """
    if not os.path.exists(backup_path):
        print(f"Резервная копия не найдена: {backup_path}")
        return
    with open(backup_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    if not lines:
        print("Резервная копия пуста.")
        return
    if lines[0].strip() != "# FamilyCalendar Backup v1.0":
        print("Неверный формат резервной копии.")
        return
    date_str = lines[1].strip()
    count = int(lines[2].strip())
    records = []
    for i in range(3, 3 + count):
        line = lines[i].strip()
        parts = line.split(':')
        if len(parts) < 5:
            print(f"Ошибка разбора строки: {line}")
            continue
        record_type, record_id, name, start_date, end_date = parts[:5]
        if record_type == 'event':
            records.append(Event(record_id, name, start_date, end_date))
        elif record_type == 'task':
            records.append(Task(record_id, name, start_date, end_date))
        elif record_type == 'reminder':
            records.append(Reminder(record_id, name, start_date, end_date))
        elif record_type == 'todo':
            records.append(Todo(record_id, name, start_date, end_date))
    print(f"Восстановлено {len(records)} записей из {backup_path}")

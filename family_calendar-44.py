# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: FamilyCalendar
def backup_data(filepath):
    """Создать резервную копию файла данных."""
    import shutil
    if not filepath or not os.path.exists(filepath):
        print("Файл данных не найден, резервное копирование отменено.")
        return None
    backup_dir = os.path.join(os.path.dirname(filepath), "backups")
    os.makedirs(backup_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"backup_{timestamp}.json")
    shutil.copy2(filepath, backup_path)
    print(f"Резервная копия сохранена: {backup_path}")
    return backup_path

# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: FamilyCalendar
def load_from_json(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, dict):
            for key in ['events', 'tasks', 'reminders']:
                if key in data and isinstance(data[key], list):
                    globals()[key] = data[key]
        elif isinstance(data, list):
            pass  # Assume flat structure or ignore
    except FileNotFoundError:
        print(f"Файл {filepath} не найден.")
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON в файле {filepath}: {e}")
    except Exception as e:
        print(f"Неожиданная ошибка при загрузке данных из {filepath}: {e}")

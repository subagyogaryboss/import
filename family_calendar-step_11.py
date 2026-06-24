# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: FamilyCalendar
import json, os

def save_to_json(data: dict, file_path: str = "family_calendar.json") -> None:
    """Сохраняет данные в JSON файл с проверкой целостности и кодировкой."""
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Данные успешно сохранены в {file_path}")
    except (json.JSONDecodeError, IOError) as e:
        print(f"Ошибка при сохранении файла: {e}")

def load_from_json(file_path: str = "family_calendar.json") -> dict | None:
    """Загружает данные из JSON файла или возвращает пустой словарь при ошибке."""
    if not os.path.exists(file_path):
        return {}
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"Данные успешно загружены из {file_path}")
        return data
    except (json.JSONDecodeError, IOError) as e:
        print(f"Ошибка при загрузке файла: {e}")
        return {}

# Пример использования в конце скрипта после заполнения данных
if __name__ == "__main__":
    # Заглушка для демонстрации вызова функций сохранения и загрузки
    sample_data = {"events": [], "tasks": []}
    save_to_json(sample_data)
    loaded_data = load_from_json()

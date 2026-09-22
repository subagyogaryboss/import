# === Stage 55: Добавь мягкую проверку дубликатов при создании записей ===
# Project: FamilyCalendar
def check_duplicate_records(records):
    """Mягкая проверка дубликатов: возвращает список записей с одинаковыми ключевыми полями."""
    duplicates = []
    seen = set()
    for r in records:
        key = tuple(sorted((r.get('name', ''), r.get('date', ''), r.get('time', ''), r.get('type', ''), r.get('parent', ''), r.get('status', '')).items()))
        if key in seen:
            duplicates.append(r)
        else:
            seen.add(key)
    return duplicates

# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: FamilyCalendar
def print_metrics():
    """Вывод ключевых метрик проекта FamilyCalendar."""
    metrics = [
        ("Семейные события", len(family_events) if family_events else 0),
        ("Обязанности", len(family_duties) if family_duties else 0),
        ("Задачи в списке дел", len(chores) if chores else 0),
    ]
    print("\n📊 Ключевые метрики FamilyCalendar:")
    for name, count in metrics:
        print(f"   {name}: {count}")

print_metrics()

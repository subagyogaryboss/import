# === Stage 60: Добавь финальную справку по командам и примеры использования ===
# Project: FamilyCalendar
def print_help():
    """Выводит справку по командам FamilyCalendar."""
    print("=" * 50)
    print("FamilyCalendar - семейный календарь")
    print("=" * 50)
    print("Доступные команды:")
    print("  add_event <название> <дата> [время] - добавить событие")
    print("  add_task <название> <ответственный> - добавить обязанность")
    print("  add_todo <название> - добавить пункт в список дел")
    print("  remind <название> <дата> - настроить напоминание")
    print("  list_events - показать все события")
    print("  list_tasks - показать все обязанности")
    print("  list_todos - показать все пункты списков дел")
    print("  list_reminders - показать все напоминания")
    print("  complete_todo <название> - отметить пункт выполненным")
    print("  remove_event <дата> - удалить событие за дату")
    print("  help - показать эту справку")
    print("=" * 50)

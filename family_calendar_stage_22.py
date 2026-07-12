# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: FamilyCalendar
def check_overdue_reminders():
    """Проверяет просроченные напоминания и возвращает список с деталями."""
    overdue = []
    now = datetime.now()
    for reminder in reminders:
        if reminder.is_set and reminder.date <= now and not reminder.checked:
            overdue.append({
                "id": reminder.id,
                "text": reminder.text,
                "due_date": reminder.date.strftime("%d.%m.%Y"),
                "days_overdue": (now - reminder.date).days if isinstance(reminder.date, datetime) else 0
            })
    return overdue

# Пример вызова:
# print("Просроченные напоминания:")
# for item in check_overdue_reminders():
#     print(f"  [{item['days_overdue']} дн.] {item['text']} — срок {item['due_date']}")

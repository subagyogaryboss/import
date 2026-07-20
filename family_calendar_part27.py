# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: FamilyCalendar
def reset_demo_data():
    """Сбрасывает демо-данные в календарь, обязанности и списки дел."""
    global events, tasks, reminders
    demo_events = [
        {"title": "День рождения мамы", "date": "2025-12-25", "type": "event"},
        {"title": "Семейный ужин", "date": "2025-12-30", "type": "event"},
        {"title": "Урок музыки", "date": "2026-01-05", "type": "task"},
    ]
    demo_tasks = [
        {"text": "Купить продукты", "done": False},
        {"text": "Помыть машину", "done": True},
        {"text": "Подготовить подарки", "done": False},
    ]
    demo_reminders = [
        {"message": "Не забыть позвонить бабушке", "time": "18:00"},
        {"message": "Встреча с врачом", "time": "20:30"},
    ]
    events.clear()
    tasks.clear()
    reminders.clear()
    events.extend(demo_events)
    tasks.extend(demo_tasks)
    reminders.extend(demo_reminders)


def clear_state():
    """Полностью очищает все данные календаря."""
    global events, tasks, reminders
    events.clear()
    tasks.clear()
    reminders.clear()

# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: FamilyCalendar
def demo_commands():
    print("=" * 50)
    print("ДЕМО-КОМАНДЫ ДЛЯ ТЕСТИРОВАНИЯ")
    print("=" * 50)

    # Команда 1: Создать события на неделю
    cal = Calendar()
    for day in range(7):
        event = Event(
            title=f"Событие дня {day + 1}",
            date=dt.date.today().replace(day=day + 1),
            description="Демо событие",
            attendees=["Alice"],
            priority=Priority.MEDIUM,
            location="Город"
        )
        cal.events.append(event)
    print("✓ Добавлено 7 событий на неделю")

    # Команда 2: Создать задачи и добавить их в список дел
    tasks = [
        Task(title="Купить молоко", deadline=dt.date.today(), priority=Priority.HIGH),
        Task(title="Помыть посуду", deadline=dt.date.today() + dt.timedelta(days=1), priority=Priority.LOW),
        Task(title="Убраться в комнате", deadline=dt.date.today() + dt.timedelta(days=2), priority=Priority.MEDIUM),
    ]
    todos = [
        TodoItem(text="Позвонить маме", completed=False, due_date=dt.date.today()),
        TodoItem(text="Сделать домашку", completed=True, due_date=dt.date.today() - dt.timedelta(days=1)),
    ]
    cal.tasks.extend(tasks)
    cal.todos.extend(todos)
    print("✓ Добавлено 3 задачи и 2 дела")

    # Команда 3: Создать напоминания
    reminders = [
        Reminder(text="Не забыть забрать документы", time=dt.datetime.now().replace(hour=10, minute=0), priority=Priority.HIGH),
        Reminder(text="Позвонить врачу", time=dt.datetime.now().replace(hour=15, minute=30), priority=Priority.MEDIUM),
    ]
    cal.reminders.extend(reminders)
    print("✓ Добавлено 2 напоминания")

    # Команда 4: Создать членов семьи и назначить роли
    members = [
        FamilyMember(name="Alice", role="Родитель"),
        FamilyMember(name="Bob", role="Ребенок"),
        FamilyMember(name="Charlie", role="Помощник"),
    ]
    cal.family_members.extend(members)
    print("✓ Добавлено 3 члена семьи")

    # Команда 5: Показываем все данные
    print(f"\n📅 Итого событий: {len(cal.events)}")
    print(f"📋 Итого задач: {len(cal.tasks)}")
    print(f"✅ Итого дел: {len(cal.todos)}")
    print(f"⏰ Итого напоминаний: {len(cal.reminders)}")
    print(f"👨‍👩‍👧‍👦 Итого членов семьи: {len(cal.family_members)}")

    return cal


if __name__ == "__main__":
    demo_commands()

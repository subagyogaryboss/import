# === Stage 47: Добавь финальную функцию demo(), которая показывает основной пользовательский сценарий ===
# Project: FamilyCalendar
def demo():
    print("=" * 60)
    print("  FamilyCalendar Demo")
    print("=" * 60)

    family = Family()
    family.add_member("Alex", "Alex", "alex@example.com")
    family.add_member("Sarah", "Sarah", "sarah@example.com")
    family.add_member("Mia", "Mia", "mia@example.com")

    today = datetime(2025, 6, 15)
    tomorrow = today + timedelta(days=1)
    next_week = today + timedelta(weeks=1)

    # События
    birthday = Event("День рождения Миши", today, "Party", "18:00", "21:00", "Alex", "Sarah", "Mia")
    family.add_event(birthday)

    football = Event("Матч футбола", tomorrow, "Stadium", "10:00", "12:00", "Alex", "Mia")
    family.add_event(football)

    # Обязанности
    chore = Chore("Помыть посуду", today, "Alex", "Mia", 1)
    family.add_chore(chore)

    # Списки дел
    grocery_list = GroceryList("Продукты", "Alex", "Mia",
        GroceryItem("Молоко", 1), GroceryItem("Хлеб", 2), GroceryItem("Яблоки", 3))
    family.add_grocery_list(grocery_list)

    # Напоминания
    reminder = Reminder("Купить цветы", next_week, "Alex", "Sarah")
    family.add_reminder(reminder)

    # Вывод
    print("\n--- Семья ---")
    print(f"  Члены: {family.get_members()}")

    print("\n--- События ---")
    for e in family.get_events():
        print(f"  • {e.title} ({e.date.date()}) — {e.time}–{e.end_time}")

    print("\n--- Обязанности ---")
    for c in family.get_chores():
        print(f"  • {c.description} — {c.assigned_to} (сегодня)")

    print("\n--- Продукты ---")
    print(f"  • {grocery_list.title}: {grocery_list.items}")

    print("\n--- Напоминания ---")
    for r in family.get_reminders():
        print(f"  • {r.description} ({r.date.date()}) — {r.assigned_to}")

    print("\nДемо завершён! Спасибо за использование FamilyCalendar.")

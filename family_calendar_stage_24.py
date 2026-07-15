# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: FamilyCalendar
def print_record(record):
    if record is None:
        print("(запись отсутствует)")
        return
    lines = []
    lines.append(f"[{record.get_date()}]")
    for key, value in record.items():
        if key != "date":
            label = key.capitalize().replace("_", " ")
            lines.append(f"  {label}: {value}")
    print("\n".join(lines))

def main():
    import sys
    sys.path.insert(0, '.')
    from family_calendar import FamilyCalendar

    cal = FamilyCalendar()
    cal.add_event("Семейный ужин", "2025-07-18 19:00")
    cal.add_task("Купить молоко", deadline="2025-07-17")
    cal.add_reminder("Вызвать врача", "2025-07-16", priority="high")

    print_record(cal.get_event("Семейный ужин"))
    print_record(cal.get_task("Купить молоко"))
    print_record(cal.get_reminder("Вызвать врача"))

if __name__ == "__main__":
    main()

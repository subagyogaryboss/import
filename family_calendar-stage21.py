# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: FamilyCalendar
class Reminder:
    def __init__(self, title, due_date):
        self.title = title
        self.due_date = due_date

    def is_overdue(self):
        return datetime.now() > self.due_date

    def __str__(self):
        status = "⚠️ overdue" if self.is_overdue() else "✅ pending"
        return f"{status}: {self.title} (until {self.due_date})"


class FamilyCalendar:
    def __init__(self, name="Family Calendar"):
        self.name = name
        self.events = []
        self.tasks = []
        self.reminders = []

    def add_event(self, title, date):
        self.events.append({"title": title, "date": date})
        return f"✅ Event added: {title} on {date}"

    def add_task(self, description, due_date):
        self.tasks.append({"description": description, "due_date": due_date})
        return f"✅ Task added: {description} (by {due_date})"

    def add_reminder(self, title, due_date):
        reminder = Reminder(title, due_date)
        self.reminders.append(reminder)
        return f"🔔 Reminder added: {title} at {due_date}"

    def get_overdue_reminders(self):
        overdue = [r for r in self.reminders if r.is_overdue()]
        return overdue


calendar = FamilyCalendar()
print(calendar.add_event("Dentist appointment", "2025-12-31"))
print(calendar.add_task("Buy groceries", "2025-12-30"))
print(calendar.add_reminder("Call mom", "2025-12-28"))
overdue = calendar.get_overdue_reminders()
if overdue:
    print("\n⚠️ Overdue reminders:")
    for r in overdue:
        print(r)
else:
    print("\n🎉 All reminders are on schedule!")

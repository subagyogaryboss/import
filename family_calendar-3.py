# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: FamilyCalendar
class FamilyCalendar:
    def __init__(self):
        self.events = []
        self.tasks = []
        self.duties = []
        self.reminders = []

    def add_event(self, title, date, description=""):
        event = {"title": title, "date": date, "description": description}
        self.events.append(event)
        return event

    def add_task(self, task_name, deadline, priority="medium"):
        task = {"task": task_name, "deadline": deadline, "priority": priority}
        self.tasks.append(task)
        return task

    def add_duty(self, person, duty_description, frequency="weekly"):
        duty = {"person": person, "duty": duty_description, "frequency": frequency}
        self.duties.append(duty)
        return duty

    def add_reminder(self, message, time, event_id=None):
        reminder = {"message": message, "time": time, "event_id": event_id}
        self.reminders.append(reminder)
        return reminder

    def get_events_by_date(self, date):
        return [e for e in self.events if e["date"] == date]

    def get_tasks_by_deadline(self, deadline):
        return [t for t in self.tasks if t["deadline"] == deadline]

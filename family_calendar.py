# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: FamilyCalendar
import datetime

class Event:
    def __init__(self, title, description="", date=None):
        self.title = title
        self.description = description
        self.date = date or datetime.date.today()

    def __str__(self):
        return f"[{self.date.strftime('%d.%m')}] {self.title}"

class FamilyCalendar:
    def __init__(self):
        self.events = []
        self.tasks = []

    def add_event(self, title, description="", date=None):
        event = Event(title, description, date)
        self.events.append(event)
        print(f"Добавлено событие: {event}")

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Добавлена задача: {task}")

    def list_events(self):
        if not self.events:
            print("Событий пока нет.")
        else:
            for e in self.events:
                print(e)

    def list_tasks(self):
        if not self.tasks:
            print("Задач пока нет.")
        else:
            for t in self.tasks:
                print(t)

def main():
    calendar = FamilyCalendar()
    
    # Демонстрационные данные
    calendar.add_event("День рождения мамы", "Купить подарок", datetime.date(2024, 12, 25))
    calendar.add_event("Сбор семьи", "Встречаемся в парке")
    calendar.add_task("Помыть посуду")
    calendar.add_task("Записаться к врачу")
    
    print("\n--- Календарь событий ---")
    calendar.list_events()
    
    print("\n--- Список задач ---")
    calendar.list_tasks()

if __name__ == "__main__":
    main()

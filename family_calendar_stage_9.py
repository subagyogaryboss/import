# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: FamilyCalendar
import json, sys, os

def load_initial_data(json_string):
    try:
        data = json.loads(json_string)
        if not isinstance(data, dict):
            raise ValueError("Invalid JSON structure")
        
        # Инициализация словарей для хранения данных, если они еще не созданы глобально
        global events, tasks, reminders
        
        # Загрузка событий (events)
        if 'events' in data:
            for event_id, event_data in data['events'].items():
                events[event_id] = {
                    'title': event_data.get('title', ''),
                    'date': event_data.get('date'),
                    'participants': event_data.get('participants', [])
                }
        
        # Загрузка задач (tasks)
        if 'tasks' in data:
            for task_id, task_data in data['tasks'].items():
                tasks[task_id] = {
                    'title': task_data.get('title', ''),
                    'assigned_to': task_data.get('assigned_to'),
                    'completed': task_data.get('completed', False)
                }
        
        # Загрузка напоминаний (reminders)
        if 'reminders' in data:
            for reminder_id, reminder_data in data['reminders'].items():
                reminders[reminder_id] = {
                    'message': reminder_data.get('message', ''),
                    'trigger_time': reminder_data.get('trigger_time')
                }
        
        print(f"Successfully loaded {len(events) + len(tasks) + len(reminders)} items from JSON string.")
    except json.JSONDecodeError as e:
        print(f"JSON parsing error: {e}")
    except Exception as e:
        print(f"Unexpected error during data loading: {e}")

# Пример использования (раскомментируйте для тестирования):
if __name__ == "__main__":
    sample_json = '''
    {
      "events": {
        "ev1": {"title": "Family Dinner", "date": "2023-12-25", "participants": ["Mom", "Dad"]}
      },
      "tasks": {
        "tsk1": {"title": "Buy groceries", "assigned_to": "Dad", "completed": false}
      },
      "reminders": {
        "rm1": {"message": "Don't forget the party!", "trigger_time": "2023-12-24T18:00"}
      }
    }
    '''
    load_initial_data(sample_json)

# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: FamilyCalendar
def export_to_json():
    import json
    from datetime import datetime
    data = {
        "version": 1,
        "timestamp": datetime.utcnow().isoformat(),
        "events": events_list.copy() if 'events_list' in globals() else [],
        "tasks": tasks_list.copy() if 'tasks_list' in globals() else [],
        "reminders": reminders_list.copy() if 'reminders_list' in globals() else []
    }
    return json.dumps(data, ensure_ascii=False, indent=2)

# === Stage 32: Добавь журнал действий пользователя ===
# Project: FamilyCalendar
class ActionLog:
    def __init__(self):
        self._entries = []

    @property
    def entries(self):
        return list(self._entries)

    def log(self, action_type, description=None, user=None, timestamp=None):
        from datetime import datetime
        record = {
            "timestamp": timestamp or datetime.now(),
            "action_type": action_type,
            "description": description,
            "user": user,
        }
        self._entries.append(record)
        return record

    def clear(self):
        self._entries.clear()

    @property
    def count(self):
        return len(self._entries)

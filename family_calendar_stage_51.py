# === Stage 51: Добавь журнал изменений данных с отметками времени ===
# Project: FamilyCalendar
class ChangeLog:
    def __init__(self, db):
        self.db = db

    def log(self, entity_type, entity_id, action, old_value=None, new_value=None):
        import datetime
        row = {
            "ts": datetime.datetime.now().isoformat(),
            "entity_type": entity_type,
            "entity_id": entity_id,
            "action": action,
            "old_value": json.dumps(old_value) if old_value is not None else None,
            "new_value": json.dumps(new_value) if new_value is not None else None,
        }
        self.db.append(row)

# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: FamilyCalendar
TEMPLATE_REGISTRY = {
    "birthday": lambda: {"title": "{name}'s Birthday", "type": "event"},
    "daily_chore": lambda: {"title": "Daily Chore: {item}", "type": "chore"},
    "reminder": lambda: {"title": "Reminder: {message}", "type": "reminder"},
    "shopping_list": lambda: {"title": "Shopping List", "type": "todo"},
}

def create_from_template(template_name, **kwargs):
    if template_name not in TEMPLATE_REGISTRY:
        raise ValueError(f"Unknown template '{template_name}'. Available: {list(TEMPLATE_REGISTRY)}")
    tpl = TEMPLATE_REGISTRY[template_name]
    record = {"title": tpl(**kwargs), "type": tpl()["type"], "created_at": datetime.now()}
    for key, val in kwargs.items():
        if key != "name" and key != "item" and key != "message":
            record[key] = val
    return _add_record(record)

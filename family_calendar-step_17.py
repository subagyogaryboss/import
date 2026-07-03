# === Stage 17: Добавь группировку записей по категориям ===
# Project: FamilyCalendar
from collections import defaultdict

def group_events_by_category(events):
    grouped = defaultdict(list)
    for event in events:
        category = event.get('category', 'other')
        grouped[category].append(event)
    return dict(grouped) if grouped else {}

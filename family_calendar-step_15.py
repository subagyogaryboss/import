# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: FamilyCalendar
def calculate_weekly_statistics(events, duties):
    if not events and not duties: return {}
    all_items = list(filter(None, events)) + list(filter(None, duties))
    week_start = min(item['date'] for item in all_items) - timedelta(days=week_start.weekday())
    week_end = week_start + timedelta(weeks=1)
    stats = defaultdict(lambda: {'count': 0, 'total_duration_minutes': 0})
    for item in all_items:
        if week_start <= item['date'] < week_end:
            duration = item.get('duration', 60)
            stats[item['category']]['count'] += 1
            stats[item['category']]['total_duration_minutes'] += duration
    return dict(stats)

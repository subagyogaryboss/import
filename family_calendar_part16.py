# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: FamilyCalendar
def calculate_monthly_statistics(events, tasks):
    from datetime import date
    stats = {}
    today = date.today()
    for year in range(today.year - 10, today.year + 2):
        for month in range(1, 13):
            key = f"{year}-{month:02d}"
            if key not in stats:
                stats[key] = {'events': 0, 'tasks_completed': 0, 'tasks_total': 0}
            
            current_month_start = date(year, month, 1)
            for event in events:
                ev_date = date.fromisoformat(event['date'])
                if ev_date.year == year and ev_date.month == month:
                    stats[key]['events'] += 1
            
            for task in tasks:
                task_date = date.fromisoformat(task.get('due_date', ''))
                if task_date.year == year and task_date.month == month:
                    stats[key]['tasks_total'] += 1
                    if task.get('completed'):
                        stats[key]['tasks_completed'] += 1
    
    return stats

# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: FamilyCalendar
def generate_summary():
    print("=== СВОДКА FAMILY CALENDAR ===")
    today = datetime.now().date()
    events_today = [e for e in all_events if e['date'] == str(today)]
    tasks_overdue = [t for t in all_tasks if t['status'] != 'done' and t['deadline'] < today]
    reminders_soon = [r for r in all_reminders if r['reminder_date'] <= today + timedelta(days=1) and not r['sent']]
    
    print(f"Сегодня ({today}): {len(events_today)} событий")
    for e in events_today[:3]:
        print(f"  - {e.get('title', 'Без названия')} в {e.get('time', '')}")
    if len(events_today) > 3:
        print(f"  ... и еще {len(events_today)-3} событий")
    
    print(f"Переданные задачи: {len(tasks_overdue)}")
    for t in tasks_overdue[:2]:
        print(f"  - [{t.get('priority', 'normal')}] {t.get('title', '')}")
    if len(tasks_overdue) > 2:
        print(f"  ... и еще {len(tasks_overdue)-2} задачи")
    
    print(f"Напоминания на сегодня/завтра: {len(reminders_soon)}")
    for r in reminders_soon[:2]:
        print(f"  - {r.get('message', '')}")
    if len(reminders_soon) > 2:
        print(f"  ... и еще {len(reminders_soon)-2} напоминания")
    
    total_tasks = sum(1 for t in all_tasks if not t['done'])
    total_events = len(all_events)
    print(f"\nИтого в системе: {total_events} событий, {total_tasks} активных задач.")

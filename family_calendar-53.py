# === Stage 53: Добавь импорт отчёта или списка записей из простого текстового формата ===
# Project: FamilyCalendar
def parse_event_file(filepath):
    """Чтение событий из текстового файла формата:
    ID;Дата(YYYY-MM-DD);Час(HH:MM);Название;Категория(с/д/о/р);Тип(событие/обязанность/напоминание/список)
    """
    events = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            parts = line.split(';')
            if len(parts) < 5:
                continue
            event_id, date_str, time_str, title, category = parts[:5]
            event_type = parts[5] if len(parts) > 5 else 'event'
            try:
                dt = datetime.strptime(date_str, '%Y-%m-%d')
                tm = datetime.strptime(time_str, '%H:%M')
            except ValueError:
                continue
            events.append({
                'id': event_id,
                'date': dt,
                'time': tm,
                'title': title,
                'category': category,
                'type': event_type,
            })
    return events

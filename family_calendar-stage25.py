# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: FamilyCalendar
def parse_date(date_str):
    """Parse date string in formats: DD.MM.YYYY, YYYY-MM-DD, or just month name."""
    import datetime
    date_str = str(date_str).strip()
    # Try DD.MM.YYYY
    for fmt in ("%d.%m.%Y", "%Y-%m-%d"):
        try:
            return datetime.datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    # Try month name (e.g., "January 25")
    date_dict = {
        'январь': 1, 'февраль': 2, 'март': 3, 'апрель': 4, 'май': 5, 'июнь': 6,
        'июль': 7, 'август': 8, 'сентябрь': 9, 'октябрь': 10, 'ноябрь': 11, 'декабрь': 12,
        'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6,
        'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12,
    }
    for month_name, month_num in date_dict.items():
        if month_name.lower() in date_str.lower():
            try:
                day = int(''.join(filter(str.isdigit, date_str)))
                return datetime.datetime(2024, month_num, day)
            except (ValueError, IndexError):
                continue
    raise ValueError(f"Некорректная дата: {date_str}. Используйте формат DD.MM.YYYY или YYYY-MM-DD")

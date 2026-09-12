# === Stage 48: Проведи рефакторинг: разнеси крупные функции, сохрани совместимость публичных команд ===
# Project: FamilyCalendar
def _format_date_range(start, end):
    """Return a human-readable date range string."""
    if start == end:
        return start.strftime("%d.%m")
    return f"{start.strftime('%d.%m')}–{end.strftime('%d.%m')}"

def _parse_date_arg(arg):
    """Convert a date string or integer to a date object."""
    if isinstance(arg, int):
        return datetime(2025, 1, 1) + timedelta(days=arg - 1)
    try:
        return datetime.strptime(arg, "%d.%m.%Y").date()
    except ValueError:
        return datetime.strptime(arg, "%d.%m").date()

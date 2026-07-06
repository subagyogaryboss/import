# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: FamilyCalendar
def archive_old_records(records, cutoff=None):
    """Archive completed or old records from the list."""
    if cutoff is None:
        cutoff = datetime.now().date() - timedelta(days=30)
    archived = []
    for rec in records:
        try:
            date_val = rec.get("date", rec.get("scheduled_date", today))
            if isinstance(date_val, str):
                date_val = datetime.strptime(date_val[:10], "%Y-%m-%d").date()
            elif isinstance(date_val, datetime):
                date_val = date_val.date()
            if date_val <= cutoff:
                archived.append(rec)
        except Exception:
            continue
    return archived

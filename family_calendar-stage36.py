# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: FamilyCalendar
def check_and_repair_data():
    """Check data integrity and repair simple issues."""
    if not isinstance(events, list):
        print("Error: events must be a list")
        return False
    
    repaired = 0
    for i in range(len(events)):
        event = events[i]
        
        # Check that each event has required fields
        if 'title' not in event or not event['title']:
            print(f"Warning: Event {i} missing title, skipping")
            continue
        
        # Check date format consistency
        if 'date' in event and isinstance(event['date'], str):
            try:
                dt = datetime.fromisoformat(event['date'])
                if dt < datetime(2024, 1, 1) or dt > datetime.now():
                    print(f"Warning: Event {i} has unusual date range")
            except ValueError:
                print(f"Warning: Event {i} has invalid date format")
    
    return repaired

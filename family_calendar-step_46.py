# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: FamilyCalendar
def migrate_data_v1(data):
    """Migration: normalize old schema to current version.
    Handles legacy 'tasks' and 'reminders' keys, merging them
    into the new unified 'events' structure with a 'type' field.
    Returns updated data dict with a 'version' key set to 1.
    """
    if not isinstance(data, dict):
        return data
    if "version" in data and data["version"] >= 1:
        return data
    migrated = {"version": 1, "events": []}
    legacy_keys = {"tasks": [], "reminders": []}
    for key, items in legacy_keys.items():
        if key in data:
            migrated["events"].extend(items)
    # Preserve existing 'events' if any
    if "events" in data:
        migrated["events"].extend(data["events"])
    # Keep any other top-level keys that are not legacy or version
    for k, v in data.items():
        if k not in legacy_keys and k != "version":
            migrated[k] = v
    return migrated

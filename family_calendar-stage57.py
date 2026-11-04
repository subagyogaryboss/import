# === Stage 57: Добавь массовое удаление с подтверждением через параметр ===
# Project: FamilyCalendar
def delete_events_promised():
    print("Массовое удаление событий. Введите ID событий через запятую (или 'q' для отмены):")
    raw = input("> ").strip()
    if raw.lower() in ("q", ""):
        return
    ids = [int(x) for x in raw.split(",") if x.strip().isdigit()]
    if not ids:
        print("Некорректный ввод. Ничего не удалено.")
        return
    if not events:
        print("Список событий пуст.")
        return
    existing = set(e["id"] for e in events)
    target = [e for e in events if e["id"] in existing]
    if not target:
        print("Ни одно из указанных событий не найдено.")
        return
    print("Удалить следующие события?")
    for e in target:
        print(f"  [{e['id']}] {e['title']} ({e['date']})")
    confirm = input("Подтвердите удаление (yes/no): ").strip().lower()
    if confirm != "yes":
        print("Отмена. События сохранены.")
        return
    kept = [e for e in events if e["id"] not in existing or e["id"] not in ids]
    events[:] = kept
    print(f"Удалено событий: {len(target)}")

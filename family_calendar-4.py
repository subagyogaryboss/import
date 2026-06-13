# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: FamilyCalendar
def edit_record(record_id, updates):
    if record_id not in records:
        print(f"Запись с ID {record_id} не найдена.")
        return False
    
    for key, value in updates.items():
        if key in record_fields and value is not None:
            records[record_id][key] = value
        elif key == 'delete':
            del records[record_id]
    
    print(f"Запись {record_id} обновлена.")
    return True

def delete_record(record_id):
    if record_id in records:
        del records[record_id]
        print(f"Запись с ID {record_id} удалена.")
        return True
    else:
        print(f"Запись с ID {record_id} не найдена для удаления.")
        return False

# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: FamilyCalendar
class ValidationError(Exception):
    pass

def validate_date(date_str):
    try:
        year, month, day = map(int, date_str.split('-'))
        if not (1 <= month <= 12 and 1 <= day <= 31):
            raise ValidationError("Некорректные день или месяц.")
        return date_str
    except ValueError:
        raise ValidationError("Дата должна быть в формате ГГГГ-ММ-ДД.")

def validate_task_description(description):
    if not description or len(description.strip()) < 3:
        raise ValidationError("Описание задачи должно содержать минимум 3 символа.")
    return description.strip()

def validate_event_title(title):
    if not title or len(title.strip()) < 2:
        raise ValidationError("Заголовок события должен содержать минимум 2 символа.")
    return title.strip()

def validate_time(time_str):
    try:
        hour, minute = map(int, time_str.split(':'))
        if not (0 <= hour <= 23 and 0 <= minute <= 59):
            raise ValidationError("Некорректное время.")
        return time_str
    except ValueError:
        raise ValidationError("Время должно быть в формате ЧЧ:ММ.")

def validate_email(email):
    if '@' not in email or '.' not in email.split('@')[1]:
        raise ValidationError("Некорректный формат email.")
    return email

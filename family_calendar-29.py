# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: FamilyCalendar
APP_CONFIG = {
    "app_name": "FamilyCalendar",
    "version": "1.0.29",
    "language": "ru",
    "theme": {
        "primary_color": "#4CAF50",
        "secondary_color": "#FF9800",
        "text_color": "#333333",
        "background_color": "#F5F5F5"
    },
    "notifications": {
        "enabled": True,
        "sound_on_success": True,
        "reminder_before_days": 1,
        "max_reminders_per_event": 2
    },
    "data": {
        "storage_path": "./family_calendar_data.json",
        "backup_enabled": False
    }
}

# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: FamilyCalendar
class Profile:
    def __init__(self, name, color="#4CAF50"):
        self.name = name
        self.color = color
        self.events = []
        self.tasks = []
        self.reminders = []
    
    @property
    def event_count(self):
        return len(self.events)
    
    @property
    def task_count(self):
        return len(self.tasks)

class ProfileManager:
    _profiles = {}
    
    @classmethod
    def get_profile(cls, name):
        if name not in cls._profiles:
            cls._profiles[name] = Profile(name)
        return cls._profiles[name]
    
    @classmethod
    def add_profile(cls, name, color="#4CAF50"):
        profile = cls.get_profile(name, color)
        return profile
    
    @classmethod
    def list_profiles(cls):
        return dict(list(cls._profiles.items()))

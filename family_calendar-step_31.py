# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: FamilyCalendar
class ProfileSwitcher:
    def __init__(self, profiles, current):
        self.profiles = {name: profile for name, profile in enumerate(profiles)}
        self.current = current

    def switch(self, new_name):
        if new_name not in self.profiles:
            return False
        self.current = new_name
        return True

    @property
    def active_profile(self):
        return self.profiles[self.current]

    def get_all_names(self):
        return list(self.profiles.keys())

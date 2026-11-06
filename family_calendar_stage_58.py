# === Stage 58: Добавь простую систему пользовательских представлений списка ===
# Project: FamilyCalendar
# Этап 58: Простая система пользовательских представлений списка
class ViewTemplate:
    def __init__(self, name, title, columns):
        self.name = name
        self.title = title
        self.columns = columns

    def render(self, items):
        if not self.columns:
            print(f"  {self.title}")
            return
        headers = self.columns + [""]
        widths = [max(len(str(h)), max([len(str(i.get(c, ""))) for i in items])) for h, c in zip(headers, self.columns)]
        print(f"  {self.title}")
        row = "  ".join(str(h).ljust(widths[i]) for i, h in enumerate(headers)).rstrip()
        print("  " + row)
        for i in items:
            row = "  ".join(str(i.get(c, "")).ljust(widths[i]) for i, c in enumerate(self.columns + [""])).rstrip()
            print("  " + row)


class ViewManager:
    def __init__(self):
        self.templates = {}

    def add_view(self, name, title, columns):
        self.templates[name] = ViewTemplate(name, title, columns)

    def get_view(self, name):
        return self.templates.get(name)

    def list_views(self):
        if not self.templates:
            print("  (нет пользовательских представлений)")
        for name, tmpl in self.templates.items():
            print(f"  [{name}] {tmpl.title} -> {tmpl.columns}")


VIEW_MANAGER = ViewManager()
VIEW_MANAGER.add_view("todos_by_person", "Дел по людям", ["person", "due_date", "status"])
VIEW_MANAGER.add_view("events_by_type", "События по типу", ["category", "start_time", "location"])
VIEW_MANAGER.add_view("chore_by_age", "Обязанности по возрасту", ["age_group", "completed"])

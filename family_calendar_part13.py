# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: FamilyCalendar
class SearchEngine:
    def __init__(self, data):
        self.data = data
    
    def search(self, query, fields=None):
        if not fields:
            fields = ['name', 'description']
        results = []
        for item in self.data:
            match_count = 0
            for field in fields:
                value = str(item.get(field, '')).lower()
                if query.lower() in value:
                    match_count += 1
            if match_count > 0:
                results.append(item)
        return results

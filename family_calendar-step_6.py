# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: FamilyCalendar
class FilteredList:
    def __init__(self, items):
        self.items = items
    
    def filter_by_status(self, status=None):
        if status is None:
            return self
        return FilteredList([item for item in self.items if getattr(item, 'status', None) == status])
    
    def filter_by_category(self, category=None):
        if category is None:
            return self
        return FilteredList([item for item in self.items if getattr(item, 'category', None) == category])
    
    def filter_by_tags(self, tags=None):
        if not tags:
            return self
        filtered = []
        for item in self.items:
            item_tags = getattr(item, 'tags', [])
            if any(tag in item_tags for tag in tags):
                filtered.append(item)
        return FilteredList(filtered)
    
    def apply_filters(self, status=None, category=None, tags=None):
        result = self.filter_by_status(status)
        result = result.filter_by_category(category)
        result = result.filter_by_tags(tags)
        return result.items

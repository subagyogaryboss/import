# === Stage 54: Добавь режим избранных записей и быстрый доступ к ним ===
# Project: FamilyCalendar
class FavoritesManager:
    def __init__(self):
        self._favorites = []
        self._next_id = 1

    def add_favorite(self, record):
        fav = {
            'id': self._next_id,
            'record': record,
            'added': datetime.now(),
            'used_count': 0,
        }
        self._favorites.append(fav)
        self._next_id += 1
        return fav

    def remove_favorite(self, fav_id):
        return self._favorites.remove(fav for fav in self._favorites if fav['id'] == fav_id)

    def get_favorites(self):
        return list(self._favorites)

    def get_recent_favorites(self, limit=5):
        return self._favorites[-limit:]

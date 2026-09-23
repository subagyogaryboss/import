# === Stage 56: Добавь массовое обновление выбранных записей ===
# Project: FamilyCalendar
def bulk_update_records(self, records: list[dict]) -> list[dict]:
        """Массовое обновление выбранных записей."""
        updated = []
        for rec in records:
            if rec.get("id") is None:
                raise ValueError("Запись должна иметь id")
            existing = self._records.get(rec["id"])
            if existing is None:
                raise ValueError(f"Запись с id={rec['id']} не найдена")
            for key, value in rec.items():
                if key not in existing or key == "id":
                    continue
                setattr(existing, key, value)
            updated.append(existing)
        self._records.update({r["id"]: r for r in updated})
        return updated

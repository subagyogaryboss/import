# === Stage 50: Сделай аккуратную финальную полировку сообщений, названий функций и комментариев ===
# Project: FamilyCalendar
def _format_event_display(event: Event, fmt: str = "default") -> str:
    """Return a human-readable representation of an event."""
    if fmt == "default":
        status = event.status.value if event.status else "unknown"
        return (
            f"[{event.title}]\n"
            f"  Дата: {event.date_str}\n"
            f"  Время: {event.time_str}\n"
            f"  Статус: {status}\n"
            f"  Описание: {event.description}"
        )
    elif fmt == "compact":
        return f"{event.title} ({event.date_str} {event.time_str} [{status}])"
    elif fmt == "emoji":
        emoji_map = {"planned": "📅", "confirmed": "✅", "completed": "🏁", "cancelled": "❌"}
        em = emoji_map.get(status, "❓")
        return f"{em} {event.title} — {event.date_str} {event.time_str}"
    return str(event)

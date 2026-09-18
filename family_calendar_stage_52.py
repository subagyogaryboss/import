# === Stage 52: Добавь экспорт краткого отчёта в текстовом формате ===
# Project: FamilyCalendar
def export_report(report: dict) -> str:
    lines = []
    lines.append("=== FamilyCalendar Report ===")
    lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("")
    lines.append(f"Total events: {report.get('events_count', 0)}")
    lines.append(f"Total tasks: {report.get('tasks_count', 0)}")
    lines.append(f"Total reminders: {report.get('reminders_count', 0)}")
    lines.append(f"Total obligations: {report.get('obligations_count', 0)}")
    lines.append("")
    if report.get("upcoming_events"):
        lines.append("--- Upcoming Events ---")
        for ev in report["upcoming_events"][:10]:
            lines.append(f"  {ev['date']} - {ev['title']}")
    lines.append("")
    if report.get("overdue_tasks"):
        lines.append("--- Overdue Tasks ---")
        for t in report["overdue_tasks"]:
            lines.append(f"  {t['name']} (due: {t['due_date']})")
    lines.append("")
    return "\n".join(lines)

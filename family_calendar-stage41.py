# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: FamilyCalendar
def dry_run(operation, *args, **kwargs):
    """Execute operation in dry-run mode: log the intended action without persisting."""
    print(f"[DRY-RUN] {operation}({', '.join(repr(a) for a in args)}) {', '.join(f'{k}={v}' for k, v in kwargs.items())}")
    return None

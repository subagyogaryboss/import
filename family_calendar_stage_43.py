# === Stage 43: Добавь пагинацию длинных списков ===
# Project: FamilyCalendar
def paginate(items, page_size=10):
    """Compact pagination helper: splits a list into fixed-size chunks."""
    total_pages = (len(items) + page_size - 1) // page_size
    for i in range(total_pages):
        start = i * page_size
        end = start + page_size
        yield items[start:end]

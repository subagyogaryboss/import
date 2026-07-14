# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: FamilyCalendar
def print_table(data, headers):
    """Выводит таблицу данных в консоль."""
    col_widths = [len(str(h)) for h in headers]
    rows = data if isinstance(data, list) else []
    for row in rows:
        for i, cell in enumerate(row[: len(headers)]):
            w = max(col_widths[i], len(str(cell))) if cell is not None else col_widths[i]
            col_widths[i] = w

    def format_row(cells):
        return '  '.join(f'{c:<{w}}' for c, w in zip(cells, col_widths))

    print('\n'.join([format_row(headers)] + [format_row(r) for r in rows]))

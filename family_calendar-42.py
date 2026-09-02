# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: FamilyCalendar
import sys

class Color:
    """ANSI-коды для цветного терминального вывода с поддержкой отключения."""
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    HIDE_CURSOR = "\033[?25l"
    SHOW_CURSOR = "\033[?25h"
    DEFAULT = "\033[0m"
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    BG_BLACK = "\033[40m"
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"
    BG_MAGENTA = "\033[45m"
    BG_CYAN = "\033[46m"
    BG_WHITE = "\033[47m"

    @staticmethod
    def is_terminal_color_supported():
        """Проверяет, поддерживает ли терминал ANSI-коды."""
        if sys.platform == "win32":
            import os
            return os.environ.get("ANSICON") is not None or os.environ.get("ConEmuANSI") == "ON"
        return True

    @staticmethod
    def set_enabled(enabled):
        Color.enabled = enabled
        if enabled:
            Color._init = None  # сбрасываем, чтобы при следующем вызове было пересоздано
        else:
            Color._init = None

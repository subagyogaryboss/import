# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: FamilyCalendar
class ActionRevert:
    """Механизм отката последнего действия для undo/redo функциональности."""
    
    def __init__(self):
        self._history = []
        self._max_history = 10
    
    def record(self, action_type, data=None):
        """Записывает действие в историю для возможного отката."""
        if len(self._history) >= self._max_history:
            self._history.pop(0)
        
        self._history.append({
            'type': action_type,
            'data': data,
            'timestamp': datetime.now()
        })
    
    def can_revert(self):
        """Проверяет, есть ли что-то для отката."""
        return len(self._history) > 0
    
    def revert(self):
        """Откатывает последнее действие и возвращает его данные."""
        if not self.can_revert():
            raise ValueError("Нет действий для отката")
        
        last_action = self._history.pop()
        return {
            'action_type': last_action['type'],
            'data': last_action['data']
        }
    
    def clear_history(self):
        """Очищает историю откатов."""
        self._history.clear()

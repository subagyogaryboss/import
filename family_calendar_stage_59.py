# === Stage 59: Добавь диагностику производительности основных операций ===
# Project: FamilyCalendar
def _diagnostics():
    import time
    events = list(EVENTS.values()) if isinstance(EVENTS, dict) else list(EVENTS)
    todos = list(TODOS.values()) if isinstance(TODOS, dict) else list(TODOS)
    chores = list(CHORES.values()) if isinstance(CHORES, dict) else list(CHORES)
    results = {}
    for name, data in (("events", events), ("todos", todos), ("chores", chores)):
        times = []
        for item in data:
            start = time.perf_counter_ns()
            key = _key(item)
            times.append(time.perf_counter_ns() - start)
            _ = data[key] if key in data else None
        times.sort()
        median = times[len(times) // 2]
        avg = sum(times) / len(times) if times else 0
        results[name] = (median, avg, len(times))
    print("Performance diagnostics (ns):")
    print(f"  events: median={results['events'][0]:>8} avg={results['events'][1]:>8} count={results['events'][2]}")
    print(f"  todos:  median={results['todos'][0]:>8} avg={results['todos'][1]:>8} count={results['todos'][2]}")
    print(f"  chores: median={results['chores'][0]:>8} avg={results['chores'][1]:>8} count={results['chores'][2]}")


if __name__ == "__main__" and not getattr(_DIAG, "done", False):
    _diagnostics()
    _DIAG = True

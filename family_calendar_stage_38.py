# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: FamilyCalendar
import unittest
from datetime import datetime, timedelta
from family_calendar import Calendar, Event, Task, Reminder, TodoList

class TestEdgeCases(unittest.TestCase):
    def test_zero_duration_event(self):
        cal = Calendar()
        event = Event(title="Instant", start=datetime.now(), duration=timedelta(0))
        cal.add_event(event)
        self.assertEqual(len(cal.events), 1)

    def test_very_long_duration(self):
        cal = Calendar()
        event = Event(title="Eternal", start=datetime.now(), duration=timedelta(days=365*100))
        cal.add_event(event)
        self.assertEqual(len(cal.events), 1)

    def test_empty_task_description(self):
        cal = Calendar()
        task = Task(title="No desc", description="")
        cal.add_task(task)
        self.assertEqual(len(cal.tasks), 1)

    def test_special_characters_in_title(self):
        cal = Calendar()
        title = "Event with & < > \" special chars"
        event = Event(title=title, start=datetime.now(), duration=timedelta(hours=1))
        cal.add_event(event)
        self.assertEqual(event.title, title)

    def test_reminder_zero_minutes(self):
        cal = Calendar()
        event = Event(title="Now", start=datetime.now(), duration=timedelta(hours=1))
        reminder = Reminder(event, minutes=0)
        cal.add_reminder(reminder)
        self.assertEqual(len(cal.reminders), 1)

    def test_todo_list_empty(self):
        cal = Calendar()
        self.assertEqual(len(cal.todo_lists), 0)
        list1 = cal.add_todo_list("Empty list")
        self.assertEqual(len(list1.items), 0)

    def test_duplicate_event_start_times(self):
        cal = Calendar()
        t = datetime.now()
        e1 = Event(title="A", start=t, duration=timedelta(hours=1))
        e2 = Event(title="B", start=t, duration=timedelta(hours=1))
        cal.add_event(e1)
        cal.add_event(e2)
        self.assertEqual(len(cal.events), 2)

    def test_overlapping_events_different_titles(self):
        cal = Calendar()
        t = datetime.now()
        e1 = Event(title="Morning", start=t, duration=timedelta(hours=2))
        e2 = Event(title="Afternoon", start=t + timedelta(hours=1), duration=timedelta(hours=2))
        cal.add_event(e1)
        cal.add_event(e2)
        overlaps = cal.find_overlapping()
        self.assertEqual(len(overlaps), 1)

    def test_negative_duration(self):
        cal = Calendar()
        event = Event(title="Negative", start=datetime.now(), duration=timedelta(hours=-1))
        cal.add_event(event)
        self.assertEqual(len(cal.events), 1)

    def test_many_events_performance(self):
        cal = Calendar()
        for i in range(500):
            cal.add_event(Event(title=f"Event {i}", start=datetime.now() + timedelta(minutes=i), duration=timedelta(hours=1)))
        self.assertEqual(len(cal.events), 500)
        overlaps = cal.find_overlapping()
        self.assertEqual(len(overlaps), 499)

    def test_reminder_with_invalid_minutes(self):
        cal = Calendar()
        event = Event(title="Test", start=datetime.now(), duration=timedelta(hours=1))
        reminder = Reminder(event, minutes=-1)
        cal.add_reminder(reminder)
        self.assertEqual(len(cal.reminders), 1)

    def test_empty_title_event(self):
        cal = Calendar()
        event = Event(title="", start=datetime.now(), duration=timedelta(hours=1))
        cal.add_event(event)
        self.assertEqual(len(cal.events), 1)

    def test_reminder_same_time(self):
        cal = Calendar()
        event = Event(title="Test", start=datetime.now(), duration=timedelta(hours=1))
        reminder = Reminder(event, minutes=0)
        cal.add_reminder(reminder)
        self.assertEqual(len(cal.reminders), 1)

    def test_overlapping_different_end_times(self):
        cal = Calendar()
        t = datetime.now()
        e1 = Event(title="A", start=t, duration=timedelta(hours=2))
        e2 = Event(title="B", start=t + timedelta(hours=1), duration=timedelta(hours=3))
        cal.add_event(e1)
        cal.add_event(e2)
        overlaps = cal.find_overlapping()
        self.assertEqual(len(overlaps), 1)

    def test_reminder_with_large_minutes(self):
        cal = Calendar()
        event = Event(title="Test", start=datetime.now(), duration=timedelta(hours=1))
        reminder = Reminder(event, minutes=1440)
        cal.add_reminder(reminder)
        self.assertEqual(len(cal.reminders), 1)

if __name__ == "__main__":
    unittest.main()

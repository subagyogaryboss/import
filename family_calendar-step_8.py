# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: FamilyCalendar
def print_menu():
    print("\n=== FamilyCalendar Menu ===")
    print("1. Add Event")
    print("2. List Events")
    print("3. Manage Chores")
    print("4. View To-Do Lists")
    print("5. Set Reminder")
    print("6. Exit")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid number, please try again.")

if __name__ == "__main__":
    events = []
    chores = {}
    todos = {"kitchen": [], "living_room": []}
    reminders = []
    
    while True:
        print_menu()
        choice = get_int("\nEnter choice (1-6): ")
        
        if choice == 1:
            name = input("Event Name: ").strip() or "Unnamed Event"
            date_str = input("Date (YYYY-MM-DD): ").strip()
            time = input("Time (HH:MM): ").strip()
            desc = input("Description: ") or ""
            events.append({"name": name, "date": date_str, "time": time, "desc": desc})
            print(f"Event '{name}' added.")
        
        elif choice == 2:
            if not events:
                print("No events scheduled.")
            else:
                for i, e in enumerate(events):
                    print(f"{i+1}. {e['date']} {e['time']}: {e['name']} - {e['desc']}")
        
        elif choice == 3:
            room = input("Room (kitchen/living_room): ").strip() or "kitchen"
            chore_name = input("Chore Name: ").strip() or f"Unspecified Chore in {room}"
            chores[room] = chores.get(room, []) + [chore_name]
            print(f"Added '{chore_name}' to {room}.")
        
        elif choice == 4:
            for room, items in todos.items():
                if not items: continue
                print(f"\n{room.capitalize()} To-Do List:")
                for item in items:
                    print(f"- [ ] {item}")
        
        elif choice == 5:
            msg = input("Reminder Message: ").strip() or "General Reminder"
            time_str = input("Time (HH:MM): ").strip()
            reminders.append({"msg": msg, "time": time_str})
            print(f"Reminder '{msg}' set for {time_str}.")
        
        elif choice == 6:
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice.")

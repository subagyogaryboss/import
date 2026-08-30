# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: FamilyCalendar
import argparse

def main():
    parser = argparse.ArgumentParser(description="Семейный календарь FamilyCalendar")
    sub = parser.add_subparsers(dest="command")
    
    cmd_event = sub.add_parser("event", help="Добавить/просмотреть событие")
    cmd_event.add_argument("--title", help="Название события")
    cmd_event.add_argument("--date", help="Дата (YYYY-MM-DD)")
    cmd_event.add_argument("--time", help="Время (HH:MM)")
    cmd_event.add_argument("--who", help="Участники")
    cmd_event.add_argument("--notes", help="Примечания")
    cmd_event.add_argument("--list", action="store_true", help="Показать список событий")
    
    cmd_task = sub.add_parser("task", help="Добавить/просмотреть задачу")
    cmd_task.add_argument("--title", help="Название задачи")
    cmd_task.add_argument("--due", help="Срок (YYYY-MM-DD)")
    cmd_task.add_argument("--done", action="store_true", help="Отметить как выполненную")
    cmd_task.add_argument("--list", action="store_true", help="Показать список задач")
    
    cmd_todo = sub.add_parser("todo", help="Добавить/просмотреть дело")
    cmd_todo.add_argument("--title", help="Название дела")
    cmd_todo.add_argument("--done", action="store_true", help="Отметить как сделанное")
    cmd_todo.add_argument("--list", action="store_true", help="Показать список дел")
    
    cmd_remind = sub.add_parser("remind", help="Добавить/просмотреть напоминание")
    cmd_remind.add_argument("--title", help="Напоминание")
    cmd_remind.add_argument("--date", help="Дата (YYYY-MM-DD)")
    cmd_remind.add_argument("--time", help="Время (HH:MM)")
    cmd_remind.add_argument("--done", action="store_true", help="Отметить как прочитанное")
    cmd_remind.add_argument("--list", action="store_true", help="Показать список напоминаний")
    
    args = parser.parse_args()
    if args.command:
        print(f"Команда: {args.command}")
        print(f"Параметры: {vars(args)}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

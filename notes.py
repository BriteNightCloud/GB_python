import argparse
import json
from datetime import datetime

def load_notes():
    try:
        with open("notes.json", "r") as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []
    return notes

def save_notes(notes):
    with open("notes.json", "w") as file:
        json.dump(notes, file)

def add_note(title, message):
    notes = load_notes()
    note = {
        "id": len(notes) + 1,
        "title": title,
        "message": message,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    notes.append(note)
    save_notes(notes)
    print("Заметка успешно добавлена!")

def edit_note(note_id, title, message):
    notes = load_notes()
    for note in notes:
        if note["id"] == note_id:
            note["title"] = title
            note["message"] = message
            note["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_notes(notes)
            print("Заметка успешно отредактирована!")
            return
    print("Заметка с указанным ID не найдена.")

def delete_note(note_id):
    notes = load_notes()
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            save_notes(notes)
            print("Заметка успешно удалена!")
            return
    print("Заметка с указанным ID не найдена.")

def list_notes():
    notes = load_notes()
    if len(notes) == 0:
        print("Нет доступных заметок.")
    else:
        for note in notes:
            print(f"ID: {note['id']}")
            print(f"Заголовок: {note['title']}")
            print(f"Тело заметки: {note['message']}")
            print(f"Дата/Время: {note['timestamp']}")
            print("=" * 30)

def parse_arguments():
    parser = argparse.ArgumentParser(description="Заметки")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add", help="Добавить заметку")
    add_parser.add_argument("--title", required=True, help="Заголовок заметки")
    add_parser.add_argument("--msg", required=True, help="Тело заметки")

    edit_parser = subparsers.add_parser("edit", help="Редактировать заметку")
    edit_parser.add_argument("id", type=int, help="ID заметки для редактирования")
    edit_parser.add_argument("--title", help="Новый заголовок для заметки")
    edit_parser.add_argument("--msg", help="Новое тело для заметки")

    delete_parser = subparsers.add_parser("delete", help="Удалить заметку")
    delete_parser.add_argument("id", type=int, help="ID заметки для удаления")

    subparsers.add_parser("list", help="Список всех заметок")

    return parser.parse_args()

def main():
    args = parse_arguments()
    
    if args.command == "add":
        add_note(args.title, args.msg)
    elif args.command == "edit":
        edit_note(args.id, args.title, args.msg)
    elif args.command == "delete":
        delete_note(args.id)
    elif args.command == "list":
        list_notes()

if __name__ == "__main__":
    main()
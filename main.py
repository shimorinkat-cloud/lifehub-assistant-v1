"""Main module for LifeHub Assistant."""

from commands import show_help
from contacts import create_contact
from notes import Note
from storage import load_data, save_data


def main() -> None:
    """Run the main application loop."""
    address_book, notebook = load_data()

    print("Welcome to LifeHub Assistant!")
    show_help()

    while True:
        command = input("\nEnter command: ").strip().lower()

        if command == "add-contact":
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            address = input("Address: ")
            birthday = input("Birthday (DD.MM.YYYY): ")

            contact = create_contact(
                name,
                phone,
                email,
                address,
                birthday,
            )

            if isinstance(contact, str):
                print(contact)
            else:
                print(address_book.add_contact(contact))

        elif command == "show-contacts":
            contacts = address_book.show_contacts()

            if not contacts:
                print("No contacts found.")
            else:
                for contact in contacts:
                    print(contact)

        elif command == "search-contact":
            query = input("Search query: ")
            results = address_book.search_contact(query)

            if not results:
                print("No contacts found.")
            else:
                for contact in results:
                    print(contact)

        elif command == "edit-contact":
            name = input("Enter contact name to edit: ")
            phone = input("New phone (leave empty to skip): ") or None
            email = input("New email (leave empty to skip): ") or None
            address = input("New address (leave empty to skip): ") or None
            birthday = input(
                "New birthday DD.MM.YYYY (leave empty to skip): "
            ) or None

            print(
                address_book.edit_contact(
                    name,
                    phone,
                    email,
                    address,
                    birthday,
                )
            )

        elif command == "delete-contact":
            name = input("Enter contact name: ")
            print(address_book.delete_contact(name))

        elif command == "birthdays":
            try:
                days = int(input("Enter number of days: "))
                results = address_book.get_upcoming_birthdays(days)

                if not results:
                    print("No upcoming birthdays.")
                else:
                    for contact in results:
                        print(contact)

            except ValueError:
                print("Please enter a valid number.")

        elif command == "add-note":
            text = input("Note text: ")
            tags_input = input("Tags (comma separated, optional): ")

            tags = [
                tag.strip()
                for tag in tags_input.split(",")
                if tag.strip()
            ]

            note = Note(text, tags)
            print(notebook.add_note(note))

        elif command == "show-notes":
            notes = notebook.show_notes()

            if not notes:
                print("No notes found.")
            else:
                for note in notes:
                    print(note)

        elif command == "search-note":
            query = input("Search query: ")
            results = notebook.search_notes(query)

            if not results:
                print("No notes found.")
            else:
                for note in results:
                    print(note)

        elif command == "edit-note":
            old_text = input("Enter note text to edit: ")
            new_text = input("New note text (leave empty to skip): ") or None
            tags_input = input(
                "New tags comma separated (leave empty to skip): "
            )

            new_tags = None
            if tags_input:
                new_tags = [
                    tag.strip()
                    for tag in tags_input.split(",")
                    if tag.strip()
                ]

            print(notebook.edit_note(old_text, new_text, new_tags))

        elif command == "delete-note":
            text = input("Enter note text: ")
            print(notebook.delete_note(text))

        elif command == "save":
            print(save_data(address_book, notebook))

        elif command == "help":
            show_help()

        elif command == "exit":
            save_data(address_book, notebook)
            print("Goodbye!")
            break

        else:
            print("Unknown command. Type 'help'.")


if __name__ == "__main__":
    main()
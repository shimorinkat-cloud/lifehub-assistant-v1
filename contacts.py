"""Contact management module for LifeHub Assistant."""

from datetime import datetime, timedelta

from validators import is_valid_birthday, is_valid_email, is_valid_phone


class Contact:
    """Class that represents one contact."""

    def __init__(
        self,
        name: str,
        phone: str,
        email: str,
        address: str,
        birthday: str,
    ) -> None:
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.birthday = birthday

    def __str__(self) -> str:
        return (
            f"Name: {self.name}, "
            f"Phone: {self.phone}, "
            f"Email: {self.email}, "
            f"Address: {self.address}, "
            f"Birthday: {self.birthday}"
        )


class AddressBook:
    """Class that stores and manages contacts."""

    def __init__(self) -> None:
        self.contacts: list[Contact] = []

    def add_contact(self, contact: Contact) -> str:
        """Add a new contact to the address book."""
        self.contacts.append(contact)
        return "Contact added successfully."

    def show_contacts(self) -> list[Contact]:
        """Return all contacts."""
        return self.contacts

    def search_contact(self, query: str) -> list[Contact]:
        """Search contacts by name, phone, email or address."""
        query = query.lower()
        return [
            contact
            for contact in self.contacts
            if query in contact.name.lower()
            or query in contact.phone.lower()
            or query in contact.email.lower()
            or query in contact.address.lower()
        ]

    def delete_contact(self, name: str) -> str:
        """Delete contact by name."""
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                return "Contact deleted successfully."

        return "Contact not found."

    def edit_contact(
        self,
        name: str,
        phone: str | None = None,
        email: str | None = None,
        address: str | None = None,
        birthday: str | None = None,
    ) -> str:
        """Edit contact fields by name."""
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                if phone:
                    if not is_valid_phone(phone):
                        return "Invalid phone number."
                    contact.phone = phone

                if email:
                    if not is_valid_email(email):
                        return "Invalid email address."
                    contact.email = email

                if address:
                    contact.address = address

                if birthday:
                    if not is_valid_birthday(birthday):
                        return "Invalid birthday format. Use DD.MM.YYYY."
                    contact.birthday = birthday

                return "Contact updated successfully."

        return "Contact not found."

    def get_upcoming_birthdays(self, days: int) -> list[Contact]:
        """Return contacts with birthdays in the next given number of days."""
        today = datetime.today().date()
        upcoming_contacts = []

        for contact in self.contacts:
            try:
                birthday_date = datetime.strptime(
                    contact.birthday, "%d.%m.%Y"
                ).date()
                birthday_this_year = birthday_date.replace(year=today.year)

                if birthday_this_year < today:
                    birthday_this_year = birthday_this_year.replace(
                        year=today.year + 1
                    )

                difference = birthday_this_year - today

                if difference <= timedelta(days=days):
                    upcoming_contacts.append(contact)

            except ValueError:
                continue

        return upcoming_contacts


def create_contact(
    name: str,
    phone: str,
    email: str,
    address: str,
    birthday: str,
) -> Contact | str:
    """Create contact after validation."""
    if not name.strip():
        return "Name cannot be empty."

    if not is_valid_phone(phone):
        return "Invalid phone number."

    if not is_valid_email(email):
        return "Invalid email address."

    if not is_valid_birthday(birthday):
        return "Invalid birthday format. Use DD.MM.YYYY."

    return Contact(name, phone, email, address, birthday)
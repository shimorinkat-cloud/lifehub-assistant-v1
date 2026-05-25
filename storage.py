"""Data storage module for LifeHub Assistant."""

import os
import pickle

from contacts import AddressBook
from notes import Notebook


DATA_DIR = "data"
DATA_FILE = os.path.join(DATA_DIR, "assistant_data.pkl")


def save_data(address_book: AddressBook, notebook: Notebook) -> str:
    """Save address book and notebook to file."""
    os.makedirs(DATA_DIR, exist_ok=True)

    data = {
        "address_book": address_book,
        "notebook": notebook,
    }

    with open(DATA_FILE, "wb") as file:
        pickle.dump(data, file)

    return "Data saved successfully."


def load_data() -> tuple[AddressBook, Notebook]:
    """Load address book and notebook from file."""
    if not os.path.exists(DATA_FILE):
        return AddressBook(), Notebook()

    try:
        with open(DATA_FILE, "rb") as file:
            data = pickle.load(file)

        address_book = data.get("address_book", AddressBook())
        notebook = data.get("notebook", Notebook())

        return address_book, notebook

    except (pickle.PickleError, EOFError, AttributeError):
        return AddressBook(), Notebook()
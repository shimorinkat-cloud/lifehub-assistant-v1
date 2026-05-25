"""Commands module for LifeHub Assistant."""


def show_help() -> None:
    """Display available commands."""
    print(
        """
Available commands:

Contacts:
  add-contact
  show-contacts
  search-contact
  edit-contact
  delete-contact
  birthdays

Notes:
  add-note
  show-notes
  search-note
  edit-note
  delete-note

System:
  save
  help
  exit
"""
    )
"""Notes management module for LifeHub Assistant."""


class Note:
    """Class that represents one note."""

    def __init__(self, text: str, tags: list[str] | None = None) -> None:
        self.text = text
        self.tags = tags if tags else []

    def __str__(self) -> str:
        tags_str = ", ".join(self.tags) if self.tags else "No tags"
        return f"Note: {self.text} | Tags: {tags_str}"


class Notebook:
    """Class that stores and manages notes."""

    def __init__(self) -> None:
        self.notes: list[Note] = []

    def add_note(self, note: Note) -> str:
        """Add new note."""
        self.notes.append(note)
        return "Note added successfully."

    def show_notes(self) -> list[Note]:
        """Return all notes."""
        return self.notes

    def search_notes(self, query: str) -> list[Note]:
        """Search notes by text or tags."""
        query = query.lower()

        return [
            note
            for note in self.notes
            if query in note.text.lower()
            or any(query in tag.lower() for tag in note.tags)
        ]

    def delete_note(self, text: str) -> str:
        """Delete note by text."""
        for note in self.notes:
            if note.text.lower() == text.lower():
                self.notes.remove(note)
                return "Note deleted successfully."

        return "Note not found."

    def edit_note(
        self,
        old_text: str,
        new_text: str | None = None,
        new_tags: list[str] | None = None,
    ) -> str:
        """Edit note text or tags."""
        for note in self.notes:
            if note.text.lower() == old_text.lower():

                if new_text:
                    note.text = new_text

                if new_tags is not None:
                    note.tags = new_tags

                return "Note updated successfully."

        return "Note not found."
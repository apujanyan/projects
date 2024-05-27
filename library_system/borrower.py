from utils.validators import String, Email


class Borrower:
    name = String()
    contact_info = Email()

    def __init__(
            self,
            name: str,
            contact_info: str
    ) -> None:
        self.name = name
        self.contact_info = contact_info
        self.borrowed_books = []
        self.borrowing_history = []

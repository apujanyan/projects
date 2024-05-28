from utils.validators import String, Number


class Movie:
    title = String()
    genre = String()
    length = Number()

    def __init__(
            self,
            title: str,
            genre: str,
            length: float
    ) -> None:
        self.title = title
        self.genre = genre
        self.length = length

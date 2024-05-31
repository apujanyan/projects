from utils.validators import String, DateTime
from datetime import datetime


class Album:
    title = String()
    artist = String()
    release_date = DateTime()

    def __init__(
            self,
            title: str,
            artist: str,
            release_date: datetime
    ) -> None:
        self.title = title
        self.artist = artist
        self.release_date = release_date

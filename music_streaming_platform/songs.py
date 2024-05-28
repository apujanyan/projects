from artist import Artist
from utils.validators import String, Number, CustomValidator


class Song:
    title = String()
    artist = CustomValidator(Artist)
    duration = Number()

    def __init__(
            self,
            title: str,
            artist: Artist,
            duration: float
    ) -> None:
        self.title = title
        self.artist = artist
        self.duration = duration

    def get_description(self) -> None:
        print(f'Song: {self.title}. ')


class RockSong(Song):
    def get_description(self) -> None:
        print(f'Rock song: {self.title}. ')


class PopSong(Song):
    def get_description(self) -> None:
        print(f'Pop song: {self.title}. ')
        
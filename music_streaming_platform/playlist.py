from utils.validators import String


class Playlist:
    name = String()

    def __init__(
            self,
            name: str
    ) -> None:
        self.name = name
        self.songs = []

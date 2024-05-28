from utils.validators import validate_type
from songs import Song
from artist import Artist


class MusicStreamingPlatform:
    def __init__(self) -> None:
        self.songs = []
        self.artists = []

    def add_song(self, song) -> None:
        validate_type(song, Song)
        self.songs.append(song)

    def add_artist(self, artist) -> None:
        validate_type(artist, Artist)
        self.artists.append(artist)

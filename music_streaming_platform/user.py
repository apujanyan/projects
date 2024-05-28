from utils.validators import String, Email, validate_type
from operations import UserOperations
from streaming_platform import MusicStreamingPlatform
from songs import Song
from artist import Artist
from playlist import Playlist


class User(UserOperations):
    name = String()
    contact_info = Email()

    def __init__(
            self,
            name: str,
            contact_info: str
    ) -> None:
        self.name = name
        self.contact_info = contact_info
        self.favourite_songs = []
        self.favourite_artists = []
        self.playlists = []

    def search_song(self, service, title) -> list:
        validate_type(service, MusicStreamingPlatform)
        validate_type(title, str)

        res = []
        for song in service.songs:
            if title == song.title:
                res.append(song)
        return res

    def listen_to_song(self, service, song) -> None:
        validate_type(service, MusicStreamingPlatform)
        validate_type(song, Song)

        print(f'{self.name} is listening to {song.title}. ')

    def create_playlist(self, name, *songs) -> Playlist:
        validate_type(name, str)
        for song in songs:
            validate_type(song, Song)

        playlist = Playlist(name)
        for song in songs:
            playlist.songs.append(song)
        self.playlists.append(playlist)
        return playlist

    def share_playlist(self, other, playlist) -> None:
        validate_type(other, type(self))
        validate_type(playlist, Playlist)

        if playlist in self.playlists:
            other.playlists.append(playlist)
            print(f'{self.name} successfully shared with {playlist.name}. ')
            return
        print(f'{self.name} does not have playlist {playlist.name}. ')

    def discover_new_artist(self, service) -> Artist | None:
        for artist in service.artists:
            if artist not in self.favourite_artists:
                return artist
        print('There is no new artists. ')

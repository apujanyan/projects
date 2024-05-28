from artist import Artist
from playlist import Playlist
from songs import *
from user import User
from streaming_platform import MusicStreamingPlatform


def main() -> None:
    streaming_platform = MusicStreamingPlatform()

    bob = User('Bob', 'bob@mail.com')
    jack = User('Jack', 'jack@mail.com')

    rock_artist = Artist('Adam', 'adam@mail.com')
    pop_artist = Artist('Tom', 'tom@mail.com')

    rock_song = RockSong('Rocky', rock_artist, 3)
    pop_song = PopSong('Poper', pop_artist, 4.5)

    rock_song.get_description()

    streaming_platform.add_song(rock_song)
    streaming_platform.add_song(pop_song)

    streaming_platform.add_artist(rock_artist)
    streaming_platform.add_artist(pop_artist)

    jack.listen_to_song(streaming_platform, pop_song)
    jacks_playlist = jack.create_playlist('Play', pop_song,
                                          rock_song)
    jack.share_playlist(bob, jacks_playlist)


if __name__ == '__main__':
    main()

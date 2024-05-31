from abc import ABC, abstractmethod


class UserOperations(ABC):
    @abstractmethod
    def search_for_song(
            self,
            service,
            song
    ):
        pass

    @abstractmethod
    def listen_to_song(
            self,
            service,
            song
    ):
        pass

    @abstractmethod
    def create_playlist(
            self,
            service,
            name
    ):
        pass

    @abstractmethod
    def add_song(
            self,
            song,
            playlist
    ):
        pass

    @abstractmethod
    def remove_song(
            self,
            song,
            playlist
    ):
        pass

    @abstractmethod
    def view_history(self):
        pass
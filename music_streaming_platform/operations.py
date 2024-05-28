from abc import ABC, abstractmethod


class UserOperations(ABC):
    @abstractmethod
    def search_song(self, service, title):
        pass

    @abstractmethod
    def discover_new_artist(self, service):
        pass

    @abstractmethod
    def listen_to_song(self, service, song):
        pass

    @abstractmethod
    def create_playlist(self, name, songs):
        pass

    @abstractmethod
    def share_playlist(self, other, name):
        pass

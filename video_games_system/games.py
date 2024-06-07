from base_models import GameBase
from utils.validators import String, DateTime
from datetime import datetime


class Adventure(GameBase):
    title = String()
    release_date = DateTime()

    def __init__(
            self,
            title: str,
            release_date: datetime
    ) -> None:
        self.title = title
        self.release_date = release_date
        self.genre = 'Adventure'

    def get_description(self) -> None:
        print(f'Adventure game {self.title}.')


class Sports(GameBase):
    title = String()
    release_date = DateTime()

    def __init__(
            self,
            title: str,
            release_date: datetime
    ) -> None:
        self.title = title
        self.release_date = release_date
        self.genre = 'Sports'

    def get_description(self) -> None:
        print(f'Sports game {self.title}.')

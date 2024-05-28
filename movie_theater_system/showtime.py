from __future__ import annotations
from utils.validators import DateTime, CustomValidator
from datetime import datetime
import theaters as th
import movie as mv


class Showtime:
    date_time = DateTime()
    movie = CustomValidator(mv.Movie)
    theater = CustomValidator(th.Theater)

    def __init__(
            self,
            movie: mv.Movie,
            theater: th.Theater,
            date_time: datetime
    ) -> None:
        self.movie = movie
        self.theater = theater
        self.date_time = date_time

    def __str__(self) -> str:
        return f'Theater: {self.theater}, Movie: {self.movie}. '

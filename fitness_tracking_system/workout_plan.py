from utils.validators import Integer


class WorkoutPlan:
    duration = Integer()

    def __init__(
            self,
            user,
            exercises: list,
            duration: int
    ) -> None:
        self.user = user
        self.exercises = exercises
        self.duration = duration

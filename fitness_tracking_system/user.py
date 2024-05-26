from utils.validators import String, Email
from fitness_tracking_operations import UserOperations
from workout_plan import WorkoutPlan
from exercise import Exercise


class User(UserOperations):
    name = String()
    contact_info = Email()

    def __init__(
            self,
            name: str,
            contact_info: str,
    ) -> None:
        self.name = name
        self.contact_info = contact_info
        self.fav_exercises = []
        self.workout_plans = []
        self.connections = []

    def create_workout_plan(self, exercises, duration):
        workout_plan = WorkoutPlan(self, exercises, duration)
        return workout_plan

    def follow_workout_plan(self, workout_plan):
        if workout_plan not in self.workout_plans:
            self.workout_plans.append(workout_plan)
        else:
            print('You already following that workout plan. ')

    def connect_other(self, other):
        if not isinstance(other, type(self)):
            raise TypeError(f'Expected {other} to be a User type!')
        if other not in self.connections:
            self.connections.append(other)
            other.connections.append(self)
            print(f'Successfully connected to {other.name}. ')

    def track_progress(self, workout_plan: WorkoutPlan):
        if not isinstance(workout_plan, WorkoutPlan):
            raise TypeError(f'Expected {workout_plan} to be a WorkoutPlan '
                            f'type!')
        if workout_plan in self.workout_plans:
            print('In progress!')
        else:
            print('Not following this workout plan!')

    def add_fav_exercise(self, exercise):
        if not isinstance(exercise, Exercise):
            raise TypeError(f'Expected {exercise} to be an Exercise type!')
        self.fav_exercises.append(exercise)
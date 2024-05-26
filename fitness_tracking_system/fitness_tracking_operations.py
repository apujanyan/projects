from abc import ABC, abstractmethod


class UserOperations(ABC):
    @abstractmethod
    def track_progress(self, workout_plan):
        pass

    @abstractmethod
    def create_workout_plan(self, exercises, duration):
        pass

    @abstractmethod
    def follow_workout_plan(self, workout_plan):
        pass

    @abstractmethod
    def connect_other(self, other):
        pass

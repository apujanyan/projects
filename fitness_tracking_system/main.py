from exercise import Cardio, Strength
from user import User


def main() -> None:
    bicep = Strength('Bicep', 'Arms')
    run = Cardio('Run', 'Legs')
    stretching = Cardio('Stretching', 'All body')

    bob = User('Bob', 'bob@mail.com')
    tom = User('Tom', 'tom@mail.com')

    tom.add_fav_exercise(run)
    bob.add_fav_exercise(stretching)

    toms_workout_plan = tom.create_workout_plan([run, stretching],
                                                90)
    bobs_workout_plan = bob.create_workout_plan([stretching],
                                                50)

    tom.follow_workout_plan(toms_workout_plan)
    bob.follow_workout_plan(bobs_workout_plan)

    tom.track_progress(toms_workout_plan)
    bob.track_progress(bobs_workout_plan)
    tom.track_progress(bobs_workout_plan)

    tom.connect_other(bob)
    print(tom.connections)
    bob.connect_other(tom)
    print(bob.connections)


if __name__ == '__main__':
    main()

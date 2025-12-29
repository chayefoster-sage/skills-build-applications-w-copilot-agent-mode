from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from octofit_tracker import models as app_models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        User = get_user_model()
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Team Marvel')
        dc = Team.objects.create(name='Team DC')

        # Create users
        users = [
            User(email='tony@stark.com', username='IronMan', team=marvel),
            User(email='steve@rogers.com', username='CaptainAmerica', team=marvel),
            User(email='bruce@wayne.com', username='Batman', team=dc),
            User(email='clark@kent.com', username='Superman', team=dc),
        ]
        for user in users:
            user.set_password('password')
            user.save()

        # Create activities
        activities = [
            Activity(user=users[0], type='Run', duration=30, distance=5),
            Activity(user=users[1], type='Swim', duration=45, distance=2),
            Activity(user=users[2], type='Cycle', duration=60, distance=20),
            Activity(user=users[3], type='Yoga', duration=50, distance=0),
        ]
        for activity in activities:
            activity.save()

        # Create workouts
        workouts = [
            Workout(user=users[0], name='Chest Day', description='Bench press, push-ups'),
            Workout(user=users[1], name='Cardio Blast', description='Running, HIIT'),
            Workout(user=users[2], name='Strength', description='Deadlift, squats'),
            Workout(user=users[3], name='Flexibility', description='Stretching, yoga'),
        ]
        for workout in workouts:
            workout.save()

        # Create leaderboard
        Leaderboard.objects.create(user=users[0], points=100)
        Leaderboard.objects.create(user=users[1], points=90)
        Leaderboard.objects.create(user=users[2], points=95)
        Leaderboard.objects.create(user=users[3], points=85)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))

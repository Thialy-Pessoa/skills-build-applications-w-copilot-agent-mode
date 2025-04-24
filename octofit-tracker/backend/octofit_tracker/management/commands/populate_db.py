from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        users = [
            User(email='john.doe@example.com', name='John Doe', password='password123'),
            User(email='jane.smith@example.com', name='Jane Smith', password='password123'),
            User(email='bob.brown@example.com', name='Bob Brown', password='password123'),
        ]
        User.objects.bulk_create(users)

        # Create teams
        team1 = Team(name='Team Alpha')
        team2 = Team(name='Team Beta')
        team1.save()
        team2.save()
        team1.members.add(users[0], users[1])
        team2.members.add(users[2])

        # Create activities
        activities = [
            Activity(user=users[0], type='Running', duration=30, date=datetime.now() - timedelta(days=1)),
            Activity(user=users[1], type='Cycling', duration=60, date=datetime.now() - timedelta(days=2)),
            Activity(user=users[2], type='Swimming', duration=45, date=datetime.now() - timedelta(days=3)),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(team=team1, points=100),
            Leaderboard(team=team2, points=80),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(user=users[0], description='Morning Run', date=datetime.now() - timedelta(days=1)),
            Workout(user=users[1], description='Evening Cycling', date=datetime.now() - timedelta(days=2)),
            Workout(user=users[2], description='Swimming Practice', date=datetime.now() - timedelta(days=3)),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))

from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='marvel')
        dc = Team.objects.create(name='dc')

        # Create Users
        tony = User.objects.create(name='Tony Stark', email='tony@marvel.com', team=marvel.name)
        steve = User.objects.create(name='Steve Rogers', email='steve@marvel.com', team=marvel.name)
        bruce = User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team=dc.name)
        clark = User.objects.create(name='Clark Kent', email='clark@dc.com', team=dc.name)

        # Create Workouts
        pushups = Workout.objects.create(name='Pushups', description='Do 20 pushups')
        running = Workout.objects.create(name='Running', description='Run 5km')

        # Create Activities
        Activity.objects.create(user=tony, type='pushups', duration=20, date=date(2023, 1, 1))
        Activity.objects.create(user=steve, type='running', duration=30, date=date(2023, 1, 2))
        Activity.objects.create(user=bruce, type='pushups', duration=25, date=date(2023, 1, 3))
        Activity.objects.create(user=clark, type='running', duration=35, date=date(2023, 1, 4))

        # Create Leaderboard
        Leaderboard.objects.create(user=tony, score=100)
        Leaderboard.objects.create(user=steve, score=90)
        Leaderboard.objects.create(user=bruce, score=95)
        Leaderboard.objects.create(user=clark, score=85)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))

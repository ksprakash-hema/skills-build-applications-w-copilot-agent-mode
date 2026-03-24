from django.db import models
from bson import ObjectId

class User(models.Model):
    _id = models.CharField(max_length=24, primary_key=True, default=lambda: str(ObjectId()), editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Team(models.Model):
    _id = models.CharField(max_length=24, primary_key=True, default=lambda: str(ObjectId()), editable=False)
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class Activity(models.Model):
    _id = models.CharField(max_length=24, primary_key=True, default=lambda: str(ObjectId()), editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    duration = models.IntegerField()
    date = models.DateField()
    def __str__(self):
        return f"{self.user.name} - {self.type}"

class Workout(models.Model):
    _id = models.CharField(max_length=24, primary_key=True, default=lambda: str(ObjectId()), editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.name

class Leaderboard(models.Model):
    _id = models.CharField(max_length=24, primary_key=True, default=lambda: str(ObjectId()), editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    def __str__(self):
        return f"{self.user.name} - {self.score}"

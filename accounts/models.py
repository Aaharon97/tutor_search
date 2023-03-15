from django.db import models
from django.contrib.auth.models import User


class TutorProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='profile')
    photo = models.ImageField(null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    follows = models.ManyToManyField(User, blank=True, related_name='followers')

    def display_follows(self):
        return ", ".join([user.username for user in self.follows.all()])

    def __str__(self):
        return self.user.username
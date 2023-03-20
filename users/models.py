from django.urls import reverse
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils import timezone


class User(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    photo = models.ImageField(null=True, blank=True, default="userAvatar.png")
    city = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    follows = models.ManyToManyField('User', blank=True, symmetrical=False, related_name='followers')
    inst_username = models.TextField(blank=True)
    tg_username = models.TextField(blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='user_groups',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='user_permissions',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
        )

    objects = UserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['-date_joined']

    def __str__(self):
        return self.email


    def display_follows(self):
        return ", ".join([user.username for user in self.follows.all()])

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_user_url(self):
        return reverse('accounts-user', args=[self.id])

    def get_user_followers_url(self):
        return reverse('accounts-user-followers', args=[self.id])

    def get_user_following_url(self):
        return reverse('accounts-user-following', args=[self.id])

    def followsCount(self):
        return len([user for user in self.follows.all()]) if [user for user in self.follows.all()] else 0

    def followersCount(self):
        return len([user for user in self.followers.all()]) if [user for user in self.followers.all()] else 0

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self):
        return self.username
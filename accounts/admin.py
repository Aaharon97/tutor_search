from django.contrib import admin
from .models import TutorProfile


@admin.register(TutorProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'photo', 'city', 'country', 'bio', 'display_follows']
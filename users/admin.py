from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserCreationForm, UserChangeForm
from .models import User


class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ("username", "first_name", "last_name", "email", "city", "country", "display_follows", "bio", "inst_username",
                    "tg_username", "is_staff", "is_active",)
    list_filter = ("username", "email", "first_name", "last_name", "city", "country",
                   "bio", "inst_username", "tg_username", "username", "email", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("username", "first_name", "last_name", "email", "city",
         "country", "follows", "bio", "inst_username", "tg_username", "password")}),
        ("Permissions", {"fields": ("is_staff",
         "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "username", "first_name", "last_name", "email", "city", "country", "bio", "follows", "inst_username", "tg_username", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
         ),
    )
    search_fields = ("username", "email")
    ordering = ("username", "email")


admin.site.register(User, UserAdmin)
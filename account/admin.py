from django.contrib import admin
from .models import UserType, User

admin.site.register(User)
admin.site.register(UserType)

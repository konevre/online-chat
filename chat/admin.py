from django.contrib import admin
from .models import Chat, Message, Profile

# Register your models here.

admin.site.register(Chat)
admin.site.register(Message)
admin.site.register(Profile)
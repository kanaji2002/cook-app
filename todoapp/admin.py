from django.contrib import admin

from todoapp.models import Task

admin.site.register(Task)

from .models import Image

admin.site.register(Image)

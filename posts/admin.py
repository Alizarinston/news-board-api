from django.contrib import admin
from . import models

admin.register(models.Post, models.Comment)(admin.ModelAdmin)

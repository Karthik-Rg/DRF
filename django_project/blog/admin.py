from django.contrib import admin
from .models import Post, Announcements, Query

# Register your models here.
admin.site.register([Post, Announcements, Query])

from django.contrib import admin
from .models import Diaries, Notice, Comment
# Register your models here.

admin.site.register(Diaries)
admin.site.register(Notice)
admin.site.register(Comment)
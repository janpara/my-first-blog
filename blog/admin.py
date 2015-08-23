from django.contrib import admin
from .models import Post, Comment, Event, Task


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Event)
admin.site.register(Task)
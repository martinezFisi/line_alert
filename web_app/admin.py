from django.contrib import admin
from .models import User, Line, QueryHistory, Notification

# Register your models here.
admin.site.register(User)
admin.site.register(Line)
admin.site.register(QueryHistory)
admin.site.register(Notification)
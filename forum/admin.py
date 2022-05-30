from django.contrib import admin

from .models import Comment, Issue, Tags, TeacherProfile, UserProfile

# Register your models here.
admin.site.register(Issue)
admin.site.register(Comment)
admin.site.register(UserProfile)
admin.site.register(TeacherProfile)
admin.site.register(Tags)

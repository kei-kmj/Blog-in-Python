from django.contrib import admin
from .models import BlogPost
from .models import UserProfile
from .models import Department, Team, Position, MeetingRoom, Meeting


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_published', 'date_updated')


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'nickname', 'department', 'team', 'position')
    search_fields = ('user', 'nickname', 'department', 'team', 'position')


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Department)
admin.site.register(Team)
admin.site.register(Position)
admin.site.register(MeetingRoom)
admin.site.register(Meeting)

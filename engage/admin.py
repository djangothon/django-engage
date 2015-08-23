from django.contrib import admin
from django.contrib.auth import get_user_model

from engage.models import UserMessage


class EngageUser(get_user_model()):
    class Meta:
        proxy = True


class UserAdmin(admin.ModelAdmin):
    change_list_template = 'admin/engage_users.html'


admin.site.register(EngageUser, UserAdmin)
admin.site.register(UserMessage)

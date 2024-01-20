from django.contrib import admin


from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from user.models import User,Farmer,Donors

# Register your models here.


class UserModelAdmin(BaseUserAdmin):
    list_display = ["id","email", "name", "is_admin","role","created_at","phone","updated_at"]
    list_filter = ["is_admin","role"]
    fieldsets = [
        ("User Credentials", {"fields": ["email", "password", "role"]}),
        ("Personal info", {"fields": ["name","phone"]}),
        ("Permissions", {"fields": ["is_admin", "groups", "user_permissions"]}),  # Add 'groups' and 'user_permissions' here
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserModelAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "password1", "password2","phone","role","name"],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["email","id"]
    filter_horizontal = []


admin.site.register(User, UserModelAdmin)
admin.site.register(Farmer)
admin.site.register(Donors)

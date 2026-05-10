from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import User
from auditlog.registry import auditlog

auditlog.register(User)

class CustomUserAdmin(UserAdmin):
    model=User
    readonly_fields=('created_at',)
    list_display=['id', 'email','first_name','last_name','phone_number','is_staff']
    search_fields=['email']
    ordering=['created_at',]
    # exclude = ('password',)

    fieldsets = (
        (None, {'fields': ('email',)}),
        
        ('Personal Info', {
            'fields': (
                'first_name',
                'last_name',
                # 'password',
                'phone_number',
                'bio',
                'profile_picture',
            )
        }),

        ('Permissions', {
            'fields': (
                'is_staff',
                'is_active',
                'is_superuser',
                # 'groups',
                # 'user_permissions',
            )
        }),


    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'first_name',
                'last_name',
                'phone_number',
                'bio',
                'profile_picture',
                'password1',
                'password2',
                'is_staff',
                'is_active',
            ),
        }),
    )
    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing existing user
            return self.readonly_fields + ('email', 'created_at')
        return self.readonly_fields

admin.site.register(User,CustomUserAdmin) 
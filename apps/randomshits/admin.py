from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import User

class CustomUserAdmin(UserAdmin):
    model=User
    readonly_fields=('password','created_at','email',)
    list_display=['email','first_name','last_name','phone_number','is_staff']
    search_fields=['email']
    ordering=['created_at',]
    exclude = ('password',)

    fieldsets = (
        (None, {'fields': ('email',)}),
        
        ('Personal Info', {
            'fields': (
                'first_name',
                'last_name',
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


admin.site.register(User,CustomUserAdmin) 
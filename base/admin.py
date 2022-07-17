import sys
sys.dont_write_bytecode = True

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from base.forms import UserCreationForm
from base.models import (User,
                        Profile,
                        Nippou,
                        Output,
                        OutputTagModel,
                        )

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class OutputAdmin(admin.ModelAdmin):
    list_display = (
        'question',
        'description',
        'created_at',
        'updated_at',
    )
    search_fields = ('question', 'description')

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)
    fieldsets = (
        (None, {
            'fields': (
                'email',
                'password',
            )
        }),
        (None, {
            'fields': (
                'date_joined',
                'username',
                'is_active',
                'is_admin',
                'teacher',
            )
        })
    )
    list_display = ('username', 'is_active')
    list_filter = ()
    ordering = ()
    filter_horizontal = ()

    # --- adminでuser作成用に追加 ---
    add_fieldsets = (
        (None, {
            'fields': ('email', 'password',),
        }),
    )
    # --- adminでuser作成用に追加 ---

    add_form = UserCreationForm

admin.site.register(User, CustomUserAdmin)
admin.site.register(Nippou)
admin.site.register(Output, OutputAdmin)
admin.site.register(OutputTagModel)
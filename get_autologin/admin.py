from django.contrib import admin

from .models import Token


@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = ('token', 'user', 'created')
    fields = ('user',)
    ordering = ('-created',)

from django.contrib import admin
from .models import members


@admin.register(members)
class MembersAdmin(admin.ModelAdmin):
    list_display = ('member_id', 'name', 'address', 'phone', 'join_date')
    search_fields = ('name', 'address', 'phone')
    ordering = ('member_id',)

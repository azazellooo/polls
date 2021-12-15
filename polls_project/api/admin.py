from django.contrib import admin

from .models import Poll


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'date_start', 'date_end']
    list_filter = ['date_start', 'date_end']
    search_fields = ['name']
    fields = ['id','name', 'date_start', 'date_end', 'description']
    readonly_fields = ['id' ,]

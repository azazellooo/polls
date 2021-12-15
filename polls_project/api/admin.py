from django.contrib import admin

from .models import Poll, Question


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'date_start', 'date_end']
    list_filter = ['date_start', 'date_end']
    search_fields = ['name']
    fields = ['id','name', 'date_start', 'date_end', 'description']
    readonly_fields = ['id' ,]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'poll', 'type', 'text']
    list_filter = ['type', 'poll']
    search_fields = ['text']
    fields = ['id','text', 'poll', 'type']
    readonly_fields = ['id' ,]


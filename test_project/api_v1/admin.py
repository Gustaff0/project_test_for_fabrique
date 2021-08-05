from django.contrib import admin
from api_v1.models import Poll, Choice, Question, AnswChecker

# Register your models here.


class PollAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'start_date', 'finish_date']
    list_filter = ['title', 'start_date']
    search_fields = ['title']
    fields = ['id', 'title', 'description', 'start_date', 'finish_date']
    readonly_fields = ['id']


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'text']
    list_filter = ['text']
    search_fields = ['text']
    fields = ['id', 'question', 'text']
    readonly_fields = ['id']


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'poll', 'text', 'type']
    list_filter = ['text', 'type']
    search_fields = ['type', 'text']
    fields = ['id', 'poll', 'text', 'type']
    readonly_fields = ['id']


class AnswerCheckerAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'question', 'choice', 'answer']
    list_filter = ['answer']
    search_fields = ['answer']
    fields = ['id', 'user', 'question', 'choice', 'answer']
    readonly_fields = ['id']


admin.site.register(Poll, PollAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(AnswChecker, AnswerCheckerAdmin)
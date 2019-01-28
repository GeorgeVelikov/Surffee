from django.contrib import admin
from nested_admin.nested import NestedTabularInline, NestedStackedInline, NestedModelAdmin
from .models import Question, Choice, Survey


class ChoiceInline(NestedTabularInline):
    model = Choice
    extra = 0


class QuestionInline(NestedTabularInline):
    model = Question
    inlines = [ChoiceInline]
    extra = 0


class QuestionAdmin(NestedModelAdmin):
    # fields = ['pub_date', 'question_text']
    fieldsets = [
        (None,               {'fields': ['question_text']}),
    ]
    inlines = [ChoiceInline]
    list_display = ['question_text']
    search_fields = ['question_text']


class SurveyAdmin(NestedModelAdmin):
    model = Survey
    inlines = [QuestionInline]


admin.site.register(Survey, SurveyAdmin)

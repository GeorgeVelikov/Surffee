from django.contrib import admin
from nested_admin.nested import NestedTabularInline, NestedModelAdmin
from django.contrib.auth.admin import UserAdmin

from .models import Question, Choice, Survey, Researcher
from .forms import ResearcherCreationForm, ResearcherChangeForm


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
    readonly_fields = ['creation_date']
    list_display = ['name', 'creator', 'creation_date', 'description','active']


class ResearcherAdmin(UserAdmin):
    add_form = ResearcherCreationForm
    form = ResearcherChangeForm
    model = Researcher
    list_display = ['email', 'username', ]


admin.site.register(Survey, SurveyAdmin)
admin.site.register(Researcher, ResearcherAdmin)

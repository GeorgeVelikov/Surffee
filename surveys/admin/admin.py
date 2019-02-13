from django.contrib import admin
from nested_admin.nested import NestedModelAdmin
from django.contrib.auth.admin import UserAdmin

from .inline import Question, Choice
from ..models import Survey, Researcher
from ..forms.users import ResearcherCreationForm, ResearcherChangeForm


class QuestionAdmin(NestedModelAdmin):
    # fields = ['pub_date', 'question_text']
    fieldsets = [
        (None,               {'fields': ['question_text']}),
    ]
    inlines = [Choice]
    list_display = ['question_text']
    search_fields = ['question_text']


class SurveyAdmin(NestedModelAdmin):
    model = Survey
    inlines = [Question]
    readonly_fields = ['creation_date']
    list_display = ['name', 'creator', 'creation_date', 'description','active']


class ResearcherAdmin(UserAdmin):
    add_form = ResearcherCreationForm
    form = ResearcherChangeForm
    model = Researcher
    list_display = ['email', 'username', ]


admin.site.register(Survey, SurveyAdmin)
admin.site.register(Researcher, ResearcherAdmin)

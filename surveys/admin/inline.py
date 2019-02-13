from nested_admin.nested import NestedTabularInline
from ..models import Question, Choice


class Choice(NestedTabularInline):
    model = Choice
    extra = 0


class Question(NestedTabularInline):
    model = Question
    inlines = [Choice]
    extra = 0

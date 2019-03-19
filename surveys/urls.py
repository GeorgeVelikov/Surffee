from django.urls import path

from .views import survey, question, choice, answer, site, annotation

app_name = 'surveys'

urlpatterns = [
    path('',
         site.index,
         name='index'),

    path('active/',
         site.active_surveys,
         name='active'),

    path('inactive/',
         site.inactive_surveys,
         name="inactive"),

    path('create/',
         survey.Create.as_view(),
         name='create'),

    path('analysis/',
         site.analysis,
         name='analysis'),

    path('toggle_active/<int:survey_id>',
         survey.ActiveToggle.as_view(),
         name='toggle_active_survey'),

    path('delete_survey/<int:survey_id>',
         survey.Delete.as_view(),
         name='delete_survey'),

    path('<int:survey_id>/results/',
         survey.Results.as_view(),
         name="results"),

    path('<int:survey_id>/',
         survey.detail,
         name="detail"),

    path('<int:survey_id>/annotate/<int:annotation_id>',
         annotation.Create.as_view(),
         name="annotate"),

    path('<int:survey_id>/annotate/<int:annotation_id>/add_all/<int:choice_id>/<str:class>/<str:word_text>',
         annotation.AddAll.as_view(),
         name="annotate_add_all"),

    path('<int:survey_id>/annotate/<int:annotation_id>/add_one/<int:choice_id>/<str:class>/<str:word_text>',
         annotation.AddOne.as_view(),
         name="annotate_add_one"),

    path('<int:survey_id>/annotate/<int:annotation_id>/delete_one/<int:choice_id>/<str:class>/<str:word_text>',
         annotation.DeleteOne.as_view(),
         name="annotate_delete_one"),

    path('<int:survey_id>/annotate/<int:annotation_id>/delete_all/<int:choice_id>/<str:class>/<str:word_text>',
         annotation.DeleteAll.as_view(),
         name="annotate_delete_all"),

    path('<int:survey_id>/add_question/',
         question.Create.as_view(),
         name='add_question'),

    path('<int:survey_id>/edit_question/<int:question_id>',
         question.Edit.as_view(),
         name='edit_question'),

    path('<int:survey_id>/delete_question/<int:question_id>',
         question.Delete.as_view(),
         name='delete_question'),

    path('<int:survey_id>/delete_choice/<int:choice_id>',
         choice.Delete.as_view(),
         name='delete_choice'),

    path('answer/<int:survey_id>/agreement/',
         answer.ResearchAgreement.as_view(),
         name='answer_research_agreement'),

    path('answer/<int:survey_id>/question/<int:question_id>/',
         answer.SurveyQuestions.as_view(),
         name='answer_survey'),
]

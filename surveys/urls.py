from django.urls import path

from .views import survey, question, choice, answer, page


app_name = 'surveys'

urlpatterns = [
    path('',
         page.index,
         name='index'),

    path('create/',
         survey.Create.as_view(),
         name='create'),

    path('toggle_active/<int:survey_id>',
         survey.ActiveToggle.as_view(),
         name='toggle_active_survey'),

    path('delete_survey/<int:survey_id>',
         survey.Delete.as_view(),
         name='delete_survey'),


    path('<int:survey_id>/results/',
         survey.Results.as_view(),
         name="results"),

    path('active/',
         page.active,
         name='active'),

    path('inactive/',
         page.inactive,
         name="inactive"),

    path('<int:survey_id>/',
         survey.detail,
         name="detail"),

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

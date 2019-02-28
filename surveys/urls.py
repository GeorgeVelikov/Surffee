from django.urls import path

from .views import page, surveys


app_name = 'surveys'

urlpatterns = [
    path('',
         page.index,
         name='index'),

    path('create/',
         surveys.SurveyCreate.as_view(),
         name='create'),

    path('toggle_active/<int:survey_id>',
         surveys.SurveyActiveToggle.as_view(),
         name='toggle_active_survey'),

    path('delete_survey/<int:survey_id>',
         surveys.SurveyDelete.as_view(),
         name='delete_survey'),


    path('<int:survey_id>/results/',
         page.Results.as_view(),
         name="results"),

    path('active/',
         page.active,
         name='active'),

    path('inactive/',
         page.inactive,
         name="inactive"),

    path('<int:survey_id>/',
         page.detail,
         name="detail"),

    path('<int:survey_id>/add_question/',
         surveys.QuestionCreate.as_view(),
         name='add_question'),

    path('<int:survey_id>/edit_question/<int:question_id>',
         surveys.QuestionEdit.as_view(),
         name='edit_question'),

    path('<int:survey_id>/delete_question/<int:question_id>',
         surveys.QuestionDelete.as_view(),
         name='delete_question'),

    path('answer/<int:survey_id>/agreement/',
         surveys.ResearchAgreement.as_view(),
         name='answer_research_agreement'),

    path('answer/<int:survey_answer_id>/question/<int:question_id>/',
         surveys.AnswerSurveyQuestions.as_view(),
         name='answer_survey'),

    path('<int:survey_id>/delete_choice/<int:choice_id>',  surveys.ChoiceDelete.as_view(), name='delete_choice'),
]

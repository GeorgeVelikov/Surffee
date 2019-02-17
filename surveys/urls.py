from django.urls import path

from .views import page, surveys


app_name = 'surveys'

urlpatterns = [
    path('', page.index, name='index'),
    path('<int:survey_id>/results/', page.results, name="results"),
    path('<int:survey_id>/', page.detail, name="detail"),
    path('<int:survey_id>/add_question/', surveys.CreateQuestion.as_view(), name='add_question'),
    path('<int:survey_id>/edit_question/<int:question_id>', surveys.EditQuestion.as_view(), name='edit_question'),
    path('answer/<int:survey_id>/question/<int:question_id>', surveys.AnswerSurvey.as_view(), name='answer_survey'),
    path('create/', surveys.CreateNewSurvey.as_view(), name='create'),
    path('active/', page.active, name='active'),
    path('inactive/', page.inactive, name="inactive"),
]

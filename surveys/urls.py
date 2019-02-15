from django.urls import path

from . import views


app_name = 'surveys'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:survey_id>/results/', views.results, name="results"),
    path('<int:survey_id>/', views.detail, name="detail"),
    path('<int:survey_id>/add_question/', views.CreateQuestion.as_view(), name='add_question'),
    path('<int:survey_id>/edit_question/<int:question_id>', views.EditQuestion.as_view(), name='edit_question'),
    path('create/', views.CreateNewSurvey.as_view(), name='create'),
    path('active/', views.active, name='active'),
    path('inactive/', views.inactive, name="inactive"),]

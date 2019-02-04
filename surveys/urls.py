from django.urls import path

from . import views


appName = "Surffee"

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:survey_id>/results/', views.results, name="results"),
    path('create/', views.CreateSurvey.as_view(), name='create')
]
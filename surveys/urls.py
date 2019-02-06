from django.urls import path

from . import views

# Do NOT add app name hear as it breaks url chain and I'll break your fingers

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:survey_id>/results/', views.results, name="results"),
    path('create/', views.CreateSurvey.as_view(), name='create')
]

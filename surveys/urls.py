from django.urls import path

from . import views

# Do NOT add app name hear as it breaks url chain and I'll break your fingers
app_name = 'surveys'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:survey_id>/results/', views.results, name="results"),
    path('<int:survey_id>/', views.detail, name="detail"),
    path('create/', views.CreateSurvey.as_view(), name='create'),
    path('active/', views.active, name='active')
]

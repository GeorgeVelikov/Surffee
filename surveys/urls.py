from django.urls import path

from . import views


appName = "Surffee"

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:survey_id>/results/', views.results, name="results"),
]
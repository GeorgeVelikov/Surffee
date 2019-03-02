from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.views.generic.base import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from surveys.views import user

handler403 = 'surveys.views.error.handler403'

urlpatterns = [
    url(r'^nested_admin/',
        include('nested_admin.urls')),

    path('',
         TemplateView.as_view(template_name='home.html'),
         name='home'),

    path('admin/',
         admin.site.urls),

    path('account/',
         user.SignUp.as_view(),
         name='signup'),

    path('account/',
         include('django.contrib.auth.urls')),

    path('surveys/',
         include('surveys.urls')),

]


urlpatterns += staticfiles_urlpatterns()

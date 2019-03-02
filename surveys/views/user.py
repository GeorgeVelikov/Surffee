from django.views.generic import CreateView
from django.urls import reverse_lazy

from ..forms.users import ResearcherCreationForm


class SignUp(CreateView):
    form_class = ResearcherCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

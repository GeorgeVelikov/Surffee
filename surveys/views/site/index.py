from django.shortcuts import render
from django.core.exceptions import PermissionDenied

from ...models.survey import Survey


def index(request):
    template = 'surveys/index.html'
    context = {}
    if not request.user.is_authenticated:  # user is not logged in
        raise PermissionDenied("User is not logged in")
    if request.user.is_authenticated:
        context['my_active_surveys'] = Survey.objects.filter(creator=request.user, active=True)
        context['my_inactive_surveys'] = Survey.objects.filter(creator=request.user, active=False)
    if request.user.is_superuser:
        context['all_active_surveys'] = Survey.objects.filter(active=True)
        context['all_inactive_surveys'] = Survey.objects.filter(active=False)
    return render(request, template, context)

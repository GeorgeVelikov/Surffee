from django.shortcuts import redirect
from django.views.generic import UpdateView

from ...models.survey import Survey
from ...forms.surveys import ResearcherCreateSurvey

from ..error import permission_user_logged_in


class Create(UpdateView):
    template_name = 'surveys/create_survey.html'
    model = Survey
    form_class = ResearcherCreateSurvey

    # can just increment id of the last survey
    def get(self, request, *args, **kwargs):
        permission_user_logged_in(request)

        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        return self.render_to_response(self.get_context_data(form=form))

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        request.POST._mutable = True
        form.data['creator'] = request.user.pk
        # currently saves the PI we want in the shape of a list which is translated to a string, fix this later w/ eval
        form.data['pi_choices'] = request.POST.getlist('pi_set')
        request.POST._mutable = False

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=True)
        return redirect('/surveys/inactive')

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

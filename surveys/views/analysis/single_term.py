from django.shortcuts import redirect
from django.views.generic import CreateView

from surveys.models import SurveyAnswer
from surveys.models.annotation import Annotation, Classification, Word
from surveys.models.survey import Survey, Question, Choice, PersonalInformation
from surveys.models.analysis import AnalysisSingle
from surveys.forms.analysis import AnalysisCreator

from django.core import serializers
from ast import literal_eval
from urllib import parse

from ...views.error import permission_user_logged_in, permission_user_owns_survey, permission_user_owns_analysis, \
                            permission_user_owns_annotation
from ...views.helper import get_age_ranges


class AnalysisSingleTerm(CreateView):
    template_name = 'analysis/single.html'
    model = Annotation
    form_class = AnalysisCreator

    def get(self, request, *args, **kwargs):
        permission_user_logged_in(request)

        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        carry_over_terms = []
        carry_over_constraints = {}

        get_variables = request.GET

        if 'analysis' in get_variables:
            analysis = AnalysisSingle.objects.get(pk=get_variables['analysis'])

            permission_user_owns_analysis(request, analysis)

            analysis_name = analysis.name
            analysis_pk = analysis.pk
            survey = Survey.objects.get(pk=analysis.survey.pk)
            annotation = Annotation.objects.get(pk=analysis.annotation.pk)
            operation = "overwrite"

            # this is a little spaghetti, be careful if you're making changes to it
            # if we have no saved terms, just put carry over as an empty list
            if analysis.terms == "":
                carry_over_terms = []
            else:
                # if we have only one saved carry over term
                if isinstance(literal_eval(analysis.terms), int):
                    carry_over_terms = [analysis.terms]
                # if we have many saved carry over terms
                else:
                    carry_over_terms = list(literal_eval(analysis.terms))

            # since carried over constraints are saved in a more verbose way, they experience no issue
            carry_over_constraints = literal_eval(analysis.constraints)

        else:
            analysis_name = get_variables['name']
            analysis_pk = 0
            survey = Survey.objects.get(pk=get_variables['survey'])
            annotation = Annotation.objects.get(pk=get_variables['annotation'])

            permission_user_owns_survey(request, survey)
            permission_user_owns_annotation(request, annotation)

            operation = "save"

        classifications = Classification.objects.filter(annotation=annotation)
        questions = Question.objects.filter(survey=survey)
        choices = Choice.objects.filter(question__in=questions)
        words = Word.objects.filter(classification__in=classifications, choice__in=choices)

        class_ids_used = []
        for w in words.values_list('classification'):
            class_ids_used.append(w[0])

        for classif in classifications:
            if classif.pk not in class_ids_used:
                classifications = classifications.exclude(pk=classif.pk)

        survey_answers = SurveyAnswer.objects.filter(survey=survey)

        pi_js_droplist = {}
        for answer in survey_answers:
            for pi in literal_eval(survey.pi_choices):
                answer_value = getattr(answer.pi_questions, pi)
                pi = pi.replace("_", " ").capitalize()
                if isinstance(answer_value, str):
                    answer_value = answer_value.capitalize()
                if pi in pi_js_droplist:
                    pi_js_droplist[pi].add(answer_value)
                else:
                    pi_js_droplist[pi] = {answer_value}

        pi_js_droplist = get_age_ranges(pi_js_droplist)

        keylist = []
        for k in pi_js_droplist.keys():
            keylist.append(k)

        # this is useful in js
        answers = literal_eval(serializers.serialize("json", survey_answers))
        for answ in answers:
            pi = PersonalInformation.objects.filter(pk=answ['fields']['pi_questions']).values()[0]
            newpi = {}
            for k in pi.keys():
                if pi[k] != '' and k != 'id':
                    nk = k.replace("_", " ").capitalize()
                    newpi[nk] = pi[k]
                    if isinstance(pi[k], str):
                        newpi[nk] = (pi[k]).capitalize()
            answ['fields']['pi_questions'] = newpi

        return self.render_to_response(
            self.get_context_data(form=form,
                                  analysis_name=analysis_name,
                                  survey=survey,
                                  classifications=classifications,
                                  classificiations_js=serializers.serialize("json", classifications),
                                  questions=serializers.serialize("json", questions),
                                  choices=serializers.serialize("json", choices),
                                  words=serializers.serialize("json", words),
                                  pi_choices=literal_eval(survey.pi_choices),
                                  answers=answers,
                                  pi_js_droplist=pi_js_droplist,
                                  constraints_keys=keylist,
                                  operation=operation,
                                  carry_over_terms=carry_over_terms,
                                  carry_over_constraints=carry_over_constraints,
                                  analysis_pk=analysis_pk,
                                  )
        )

    def post(self, request, *args, **kwargs):
        if "delete" in request.POST:
            analysis_pk = request.POST['delete']

            analysis = AnalysisSingle.objects.get(pk=analysis_pk)

            analysis.delete()
            return redirect('./')

        else:
            terms = request.POST['terms']
            constraints = {}

            # transform js serialized dict to a normal py dict
            con_post = parse.parse_qs(request.POST['constraints'])
            for key in con_post.keys():
                nk = key.replace("[]", "")
                constraints[nk] = con_post[key]

            if request.POST['operation'] == "save":

                analysis_name = request.GET['name']
                analysis_survey = Survey.objects.get(pk=request.GET['survey'])
                analysis_annotation = Annotation.objects.get(pk=request.GET['annotation'])

                new_analysis = AnalysisSingle.objects.create(creator=request.user,
                                                             name=analysis_name,
                                                             survey=analysis_survey,
                                                             annotation=analysis_annotation,
                                                             terms=terms,
                                                             constraints=constraints)
                new_analysis.save()

                redirect_pk = new_analysis.pk
                return redirect('./single?analysis=' + str(redirect_pk))

            elif request.POST['operation'] == "overwrite":
                analysis_pk = request.GET['analysis']

                analysis = AnalysisSingle.objects.get(pk=analysis_pk)
                analysis.terms = terms
                analysis.constraints = constraints
                analysis.save()

                redirect_pk = analysis.pk
                return redirect('./single?analysis=' + str(redirect_pk))

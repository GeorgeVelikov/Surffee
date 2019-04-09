from django.shortcuts import redirect
from django.views.generic import CreateView

from surveys.models import SurveyAnswer
from surveys.models.annotation import Annotation, Classification, Word
from surveys.models.survey import Survey, Question, Choice
from surveys.forms.analysis import AnalysisCreator

from django.core import serializers
from ast import literal_eval


class Create(CreateView):
    template_name = 'analysis/create_analysis.html'
    model = Annotation
    form_class = AnalysisCreator
    
    def get(self, request, *args, **kwargs):
        self.object = None
        all_user_surveys = Survey.objects.filter(creator=request.user)

        form_class = self.get_form_class()
        form = self.get_form(form_class)

        all_annotations = Annotation.objects.filter(creator=request.user)
        classifications = Classification.objects.filter(annotation__in=all_annotations)
        words = Word.objects.filter(classification__in=classifications)

        used_annotations = dict()

        for word in words:
            for survey in all_user_surveys:
                if word.choice.question.survey.pk == survey.pk:
                    annot_id = word.classification.annotation.pk
                    annot_name = word.classification.annotation.name
                    if survey.pk not in used_annotations:
                        used_annotations.update({survey.pk: [[annot_id, annot_name]]})
                    else:
                        used_annotations[survey.pk].append([annot_id, annot_name])

        return self.render_to_response(
            self.get_context_data(form=form,
                                  all_user_surveys=all_user_surveys.values('pk', 'name'),
                                  used_annotations_all_surveys=used_annotations,
                                  )
        )

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        analysis_type = form.data['analysis_option']
        analysis_name = form.data['analysis_name']
        analysis_survey = form.data['survey_to_analyse']
        analysis_annot = form.data['annotation_to_analyse']

        post_variables = '?name=' + analysis_name + '&survey=' + analysis_survey + '&annotation=' + analysis_annot

        if analysis_type == "single":
            return redirect('/surveys/analysis/single' + post_variables)
        elif analysis_type == "multiple":
            return redirect('/surveys/analysis/multiple' + post_variables)
        elif analysis_type == "graph":
            return redirect('/surveys/analysis/graph' + post_variables)

        # this is in case something goes wrong, just returns back to the same page
        return redirect('/surveys/analysis')


class AnalysisSingleTerm(CreateView):
    template_name = 'analysis/single.html'
    model = Annotation
    form_class = AnalysisCreator

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        get_variables = request.GET

        analysis_name = get_variables['name']
        survey_name = Survey.objects.get(pk=get_variables['survey'])
        annotation = Annotation.objects.get(pk=get_variables['annotation'])

        classifications = Classification.objects.filter(annotation=annotation)
        questions = Question.objects.filter(survey=survey_name)
        choices = Choice.objects.filter(question__in=questions)
        words = Word.objects.filter(classification__in=classifications, choice__in=choices)

        class_ids_used = []
        for w in words.values_list('classification'):
            class_ids_used.append(w[0])

        for classif in classifications:
            if classif.pk not in class_ids_used:
                classifications = classifications.exclude(pk=classif.pk)

        survey_answers = SurveyAnswer.objects.filter(survey=survey_name)

        """
        for answer in survey_answers:
            for pi in literal_eval(survey_name.pi_choices):
                print(getattr(answer.pi_questions, pi))
        """

        return self.render_to_response(
            self.get_context_data(form=form,
                                  analysis_name=analysis_name,
                                  survey_name=survey_name,
                                  classifications=classifications,
                                  choices=serializers.serialize("json", choices),
                                  words=serializers.serialize("json", words),
                                  pi_choices=literal_eval(survey_name.pi_choices),
                                  answers=serializers.serialize("json", survey_answers),
                                  )
        )


class AnalysisMultipleTerm(CreateView):
    template_name = 'analysis/multi.html'
    model = Annotation
    form_class = AnalysisCreator

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        all_surveys = Survey.objects.filter(creator=request.user).values('pk', 'name')

        return self.render_to_response(
            self.get_context_data(form=form,
                                  all_surveys=all_surveys,
                                  )
        )

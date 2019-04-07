from django import forms

from surveys.models.annotation import Annotation


class AnalysisCreator(forms.ModelForm):
    analysis_name = forms.CharField(required=False, max_length=2**6)

    analysis_name.widget.attrs['class'] = "form-control"
    analysis_name.widget.attrs['placeholder'] = "Analysis name eg. Food survey analysis"
    analysis_name.widget.attrs['aria-label'] = "Username"
    analysis_name.widget.attrs['aria-describedby'] = "basic-addon1"

    class Meta:
        model = Annotation
        exclude = ['']

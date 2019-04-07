from django import forms
from ..models.annotation import Annotation


class AnnotationWordForm(forms.ModelForm):
    classification_name = forms.CharField(required=False, max_length=2**6)

    classification_name.widget.attrs['class'] = "textinput textInput form-control"
    classification_name.widget.attrs['placeholder'] = "Please enter a classification"

    def __init__(self, *args, **kwargs):
        super(AnnotationWordForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = False
        self.fields['name'].widget.attrs['class'] = 'annotation_name'

    class Meta:
        model = Annotation
        exclude = ['']

    def save(self, commit=True):
        return super(AnnotationWordForm, self).save(commit=commit)
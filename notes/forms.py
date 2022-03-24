from django import forms
from .models import Subject,Note


class SubjectForm(forms.ModelForm):
    name = forms.CharField(label='')

    class Meta:
        model = Subject
        fields = ('name',)

class createNotesForm(forms.ModelForm):
    class Meta:
        model = Note
        fields='__all__'
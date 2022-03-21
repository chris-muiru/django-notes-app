from django import forms
from .models import Subject


class SubjectForm(forms.ModelForm):
    name = forms.CharField(label='')
    date_created = forms.DateField(label='')

    class Meta:
        model = Subject
        fields = ('name', 'date_created')

      
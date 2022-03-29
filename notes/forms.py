from django import forms
from .models import Note


# class SubjectForm(forms.ModelForm):
#     name = forms.CharField(label='')

#     class Meta:
#         model = Subject
#         fields = ('name',)

class createNotesForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('topic', 'Notes', 'subject')
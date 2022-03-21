from django.shortcuts import render
from .models import Subject
from .forms import SubjectForm


def list_create_subject(request):
    form = SubjectForm()
    if request.method == 'POST':
        print(request.POST)
        form = SubjectForm(request.POST)
        if form.is_valid():
            print('it is valid')
            form.save()
        else:
            print('not')

    context = {
        'form': form
    }
    return render(request, 'notes/subject_pages/subject.html', context)


# Crud architecture for
# Create your views here.

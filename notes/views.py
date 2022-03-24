from django.shortcuts import render, redirect
from .models import Subject, Note
from .forms import SubjectForm, createNotesForm


def list_create_subject_view(request):
    form = SubjectForm()
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid() and not Subject.objects.filter(name=form.cleaned_data['name']).exists():
            form.save()
    subject_query_set = Subject.objects.all()
    context = {
        'form': form,
        'subjects': subject_query_set
    }
    return render(request, 'subject_page/subject.html', context)


def create_notes_view(request):
    form = createNotesForm()
    if request.method == 'POST':
        form = createNotesForm(request.POST)
        if form.is_valid():
            topic = form.cleaned_data['topic']
            if not Note.objects.filter(topic__icontains=topic).exists():
                form.save()
        return redirect('dashboard')
    context = {
        'form': form
    }
    return render(request, 'notes/createNote.html', context)


def dashboard_view(request):
    note_queryset = Note.objects.all()
    content = {
        'notes': note_queryset
    }
    return render(request, 'notes/dashboard.html', content)


def note_view(request, pk):
    query_note = Note.objects.filter(id=pk).get()
    print(query_note)

    if request.method == 'POST':
        query_note.delete()
        return redirect('dashboard')
    context = {
        'note': query_note
    }
    return render(request, 'notes/note.html', context)

# Crud architecture for
# Create your views here.

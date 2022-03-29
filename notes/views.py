from django.shortcuts import render, redirect
from .models import Note
from .forms import createNotesForm
from django.contrib.auth.decorators import login_required
from .decorators import can_delete

@login_required(login_url='login')
def create_notes_view(request):
    form = createNotesForm()
    if request.method == 'POST':
        form = createNotesForm(request.POST)
        if form.is_valid():
            topic = form.cleaned_data['topic']
            if not Note.objects.filter(topic__icontains=topic).exists():
                instance = form.save(commit=False)
                instance.user = request.user
                instance.save()
        return redirect('dashboard')
    context = {
        'form': form
    }
    return render(request, 'notes/createNote.html', context)


@login_required(login_url='login')
def dashboard_view(request):
    note_queryset = Note.objects.all()
    user=request.user
    content = {
        'notes': note_queryset,
    }
    return render(request, 'notes/dashboard.html', content)


@login_required(login_url='login')
def ListNoteView(request, pk):
    query_note = Note.objects.filter(id=pk).get()
    # if request.method == 'POST':
    #     query_note.delete()
    #     return redirect('dashboard')
    context = {
        'note': query_note
    }
    return render(request, 'notes/note.html', context)

@can_delete
def DeleteNoteView(request,pk):
    query_note = Note.objects.get(id=pk)
    query_note.delete()
    return redirect('dashboard')
     




# @login_required(login_url='login')
# def list_create_subject_view(request):
#     form = SubjectForm()
#     if request.method == 'POST':
#         form = SubjectForm(request.POST)
#         if form.is_valid() and not Subject.objects.filter(name=form.cleaned_data['name']).exists():
#             form.save()
#     subject_query_set = Subject.objects.all()
#     context = {
#         'form': form,
#         'subjects': subject_query_set
#     }
#     return render(request, 'subject_page/subject.html', context)


# Crud architecture for
# Create your views here.
#

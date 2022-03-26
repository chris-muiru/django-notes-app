from django.urls import path
from .views import list_create_subject_view, create_notes_view, dashboard_view,ListDeleteNoteView

urlpatterns = [
    path('dashboard/', dashboard_view, name="dashboard"),
    path('create-subject/', list_create_subject_view, name="create-subject"),
    path('create-note/', create_notes_view, name='create-note'),
    path('note/<int:pk>/',ListDeleteNoteView,name='note')
]

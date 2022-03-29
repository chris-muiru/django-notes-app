from django.urls import path
from .views import create_notes_view, dashboard_view,ListNoteView,DeleteNoteView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('dashboard/', dashboard_view, name="dashboard"),
    path('create-note/', create_notes_view, name='create-note'),
    path('note/<int:pk>/',ListNoteView,name='note'),
    path('delete/<int:pk>/',DeleteNoteView,name='delete-note')
]
# path('create-subject/', list_create_subject_view, name="create-subject"),

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from .models import Note
from django.shortcuts import redirect
# delete file ba only if user


def can_delete(func):
    def wrapper_can_delete(request, pk, *args, **kwargs):
        if str(Note.objects.get(id=pk).user.username) == str(request.user):
            return func(request, pk, *args, **kwargs)
        else:
            return redirect('dashboard')

    return wrapper_can_delete

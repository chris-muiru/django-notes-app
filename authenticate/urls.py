from django.urls import path
from .views import registerView,logIn,logOut
urlpatterns = [
    path('sign-up/', registerView, name='register'),
    path('sign-in/', logIn, name='login'),
    path('logout/',logOut,name="logout")
]

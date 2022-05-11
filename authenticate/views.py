from django.shortcuts import render, redirect
from .forms import RegisterUserForm,ProfileForm
from django.contrib.auth import login, authenticate, logout
from .models import Profile

def registerView(request):
    form = RegisterUserForm()
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save() # returns created user
            return redirect('login')

    context = {
        'form': form
    }
    return render(request, 'authenticate/signup.html', context)

# login user


def logIn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            pass

    context = {}
    return render(request, 'authenticate/signin.html', context)

def logOut(request):
    logout(request)
    return redirect('login')


def updateProfile(request,pk):
    query=Profile.objects.get(id=pk)
    form=ProfileForm()
    if request.method =='POST':
        form=ProfileForm(request.POST,request.FILES,instance=query)
        if form.is_valid(): 
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
        else:
            form=ProfileForm(request.POST,request.FILES,instance=query)
    context={
        'form':form
    }
    return render(request,'authenticate/profile.html',context)

# Create your views here.

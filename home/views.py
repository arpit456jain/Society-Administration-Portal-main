from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
# from django.contrib import messages

def home(request):
    return render(request,'index.html')
def dashboard(request):
    return render(request,'Pages/dashboard.html')
def gallery(request):
    return render(request,'Pages/gallery.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = user = User.objects.create_user(username, 'email', password)
        user.save()
    else:
        print("get")
        
    return render(request,"/")

def loginuser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('/')
        else:
            print("invalid")
    return render(request,"/dashboard")

def logoutuser(request):
    logout(request)
    return redirect('/')

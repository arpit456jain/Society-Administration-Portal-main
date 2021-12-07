from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from home.models import Contact,Notices
# from django.contrib import messages

def home(request):
    return render(request,'index.html')
def dashboard(request):
    return render(request,'Pages/dashboard.html')

def notices(request):
    # we have to fect all notices
    allnotices = Notices.objects.all()
    params = {'allnotices': allnotices}
    return render(request,'Pages/notices.html',params)

def map(request):
    return render(request,'Pages/map.html')

def calendar(request):
    return render(request,'Pages/calendar.html')

def gallery(request):
    return render(request,'Pages/gallery.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        pnumber = request.POST['pnumber']
        print(username, password,email,pnumber)
        user = user = User.objects.create_user(username, email, password)
        user.save()
    else:
        print("get")
        
    return redirect('/')

def loginuser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("login")
            # Redirect to a success page.
            return redirect('/dashboard')
        else:
            print("invalid")
    return redirect('/')

def logoutuser(request):
    logout(request)
    return redirect('/')

from django.shortcuts import redirect,render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,"authentication/index.html")

def signup(request):
    if(request.method=="POST"):
        username=request.POST.get('uname')
        email=request.POST.get('mail')
        password=request.POST.get('psw')
        password1=request.POST.get('psw1')
        
        myuser=User.objects.create_user(username,email,password)

        myuser.save()
        messages.success(request,"you are successfully registered.")
        return redirect('signin')

    return render(request,"authentication/signup.html")

def signin(request):
    return render(request,"authentication/signin.html")

def signout(request):
    pass
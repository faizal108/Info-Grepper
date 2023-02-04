from django.shortcuts import redirect,render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

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
    if request.method == 'POST':
        username = request.POST['uname']
        pass1 = request.POST['psw']
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            name = user.username
            # messages.success(request, "Logged In Sucessfully!!")
            return render(request, "authentication/index.html",{"name":name})
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('home')
    
    return render(request, "authentication/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('home')
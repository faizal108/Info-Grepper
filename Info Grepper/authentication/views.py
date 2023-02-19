from django.shortcuts import redirect,render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
# def home(request):
#     return render(request,"authentication/index.html")
def home(request):
    return render(request,"authentication/index.html")

def signup(request):
    if(request.method=="POST"):
        username=request.POST.get('uname')
        email=request.POST.get('mail')
        password=request.POST.get('psw')
        password1=request.POST.get('psw1')
        
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('home')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('home')
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('home')
        
        if password != password1:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('home')
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('home')

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
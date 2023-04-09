from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm
from .models import Tool


def home(request):
    return render(request, 'users/landing_page.html')

def tools(request):
    tools = Tool.objects.all()
    return render(request, 'users/tools.html', {'tools': tools})

def dashboard(request):
    return render(request, 'dashboard/dashboard-landing.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignupForm()
        
    context = { 'form': form }
    return render(request, 'users/signup.html', context)

# def all_tools(request):
#     tools = Tool.objects.all()
#     return render(request, 'tools/all_tools.html', {'tools': tools})


# @login_required
# def profile(request):
#     if request.method == 'POST':
#         # handle form submission
#         user_form = UserUpdateForm(request.POST, instance=request.user)
#         password_form = PasswordChangeForm(request.user, request.POST)
#         if user_form.is_valid() and password_form.is_valid():
#             user = user_form.save()
#             update_session_auth_hash(request, user)  # important!
#             password_form.save()
#             messages.success(request, 'Your profile was successfully updated!')
#             return redirect('dash-profile')
#     else:
#         # show form
#         user_form = UserUpdateForm(instance=request.user)
#         password_form = PasswordChangeForm(request.user)
#     return render(request, 'dashboard/profile.html', {
#         'user_form': user_form,
#         'password_form': password_form,
#     })




# def change_password(request):
#     if request.method == 'POST':
#         # Authenticate the user with their current password
#         user = authenticate(username=request.user.username, password=request.POST.get('old_password'))

#         # If authentication was successful, update the password
#         if user is not None:
#             user.set_password(request.POST.get('new_password'))
#             user.save()

#             # Update the session auth hash to prevent the user from being logged out
#             update_session_auth_hash(request, user)

#             # Redirect the user to a success page
#             messages.success(request, 'Your password has been changed successfully.')
#             return redirect('password_change_done')

#         # If authentication failed, show an error message
#         else:
#             messages.error(request, 'Your old password was entered incorrectly. Please try again.')

#     return render(request, 'change_password.html')


# ipgeo file download
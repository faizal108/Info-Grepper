from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from users.forms import UserUpdateForm
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm


# @login_required
def profile(request):
    if request.method == 'POST':
        # handle form submission
        messages.success(request, 'you click on button!!')
        user_form = UserUpdateForm(request.POST, instance=request.user)
        password_form = PasswordChangeForm(request.user, request.POST)
        if user_form.is_valid() and password_form.is_valid():
            user = user_form.save()
            update_session_auth_hash(request, user)  # important!
            password_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the errors below.')
            return redirect('profile')
    else:
        # show form
        user_form = UserUpdateForm(instance=request.user)
        password_form = PasswordChangeForm(request.user)
    return render(request, 'dashboard/profile.html', {
        'user_form': user_form,
        'password_form': password_form,
    })
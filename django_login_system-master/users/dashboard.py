from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required

from users.models import Tool
from .forms import ToolForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm


@login_required
def profile(request):
    if request.method == 'POST':
        if 'update_profile' in request.POST:
            # handle profile form submission
            user_form = UserUpdateForm(request.POST, instance=request.user)
            if user_form.is_valid():
                user = user_form.save()
                update_session_auth_hash(request, user)  # important!
                messages.success(request, 'Your profile was successfully updated!')
            else:
                messages.error(request, 'Please correct the errors below.')
        elif 'change_password' in request.POST:
            # handle password change form submission
            user = request.user
            password_form = PasswordChangeForm(user, request.POST)
            is_valid_str = str(password_form.is_valid())
            if password_form.is_valid():
                user.set_password(password_form.cleaned_data['new_password1'])
                user.save()
                update_session_auth_hash(request, user)  # important!
                messages.success(request, 'Your password was successfully changed!')
            else:
                messages.error(request, password_form.errors)
        else:
            messages.error(request, 'Invalid request.')
        return redirect(reverse('profile'))
    else:
        # show form
        user_form = UserUpdateForm(instance=request.user)
        password_form = PasswordChangeForm(request.user)
    return render(request, 'dashboard/profile.html', {
        'user_form': user_form,
        'password_form': password_form,
    })

def add_tool(request):
    if request.method == 'POST':
        form = ToolForm(request.POST)
        if form.is_valid():
            tool = form.save(commit=False)
            tool.save()
            return redirect('alltools')
    else:
        form = ToolForm()
    return render(request, 'dashboard/add_tool.html', {'form': form})

def favorite_tools(request):
    favorite_tools = Tool.objects.filter(is_favorite=True)
    return render(request, 'dashboard/favorite_tools.html', {'favorite_tools': favorite_tools})
# @login_required
# def profile(request):
#     if request.method == 'POST':
#         # handle form submission
#         messages.success(request, 'you click on button!!')
#         user_form = UserUpdateForm(request.POST, instance=request.user)
#         password_form = PasswordChangeForm(request.user, request.POST)
#         if user_form.is_valid():
#             user = user_form.save()
#             update_session_auth_hash(request, user)  # important!
#             password_form.save()
#             messages.success(request, 'Your profile was successfully updated!')
#             return redirect(reverse('profile'))
#         else:
#             messages.error(request, 'Please correct the errors below.')
#             return redirect(reverse('profile'))
#     else:
#         # show form
#         user_form = UserUpdateForm(instance=request.user)
#         password_form = PasswordChangeForm(request.user)
#     return render(request, 'dashboard/profile.html', {
#         'user_form': user_form,
#         'password_form': password_form,
#     })
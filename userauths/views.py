from django.shortcuts import render, redirect
from userauths.forms import UserRegisterForm
from django.contrib.auth import login, authenticate
from django.contrib import messages


def register_view(request):

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f'Привет, {username}! Регистрация прошла успешно.')
            login(request, new_user)
            return redirect('core:home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()

    context = {
        'form': form,
    }
    return render(request, "userauths/sign-up.html", context)

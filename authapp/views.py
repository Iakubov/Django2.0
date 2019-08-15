from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from authapp.forms import ShopUserLoginForm, ShopUserRegisterForm, ShopUserUpdateForm


def login(request):
    next = request.GET['next'] if 'next' in request.GET.keys() else None
    if request.method == 'POST':
        form = ShopUserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                next = request.POST['next'] if 'next' in request.POST.keys() else None
                print(f'next: {next}')
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index') if not next else next)
    else:
        form = ShopUserLoginForm()

    context = {
        'title': 'вход в систему',
        'form': form,
        'next': next,
    }
    return render(request, 'authapp/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


def register(request):
    if request.method == 'POST':
        form = ShopUserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        form = ShopUserRegisterForm()

    content = {
        'title': 'Sign up',
        'form': form
    }

    return render(request, 'authapp/register.html', content)


def update(request):
    if request.method == 'POST':
        form = ShopUserUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('auth:update'))
    else:
        form = ShopUserUpdateForm(instance=request.user)

    context = {
        'title': 'Update',
        'form': form
    }
    return render(request, 'authapp/update.html', context)
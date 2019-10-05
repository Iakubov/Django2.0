from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
from authapp.forms import ShopUserLoginForm, ShopUserRegisterForm, ShopUserUpdateForm
from authapp.models import ShopUser


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
                # print(f'next: {next}')
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index') if not next else next)
    else:
        form = ShopUserLoginForm()

    context = {
        'title': 'Login',
        'form': form,
        'next': next,
    }
    return render(request, 'authapp/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:index'))


def register(request):
    if request.method == 'POST':
        form = ShopUserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            if send_verify_mail(user):
                print('EMAIL SENT')
                return HttpResponseRedirect(reverse('auth:login'))
            else:
                print('EMAIL ERROR')
                return HttpResponseRedirect(reverse('auth:login'))
    else:
        form = ShopUserRegisterForm()

    context = {
        'title': 'Sign up',
        'form': form
    }

    return render(request, 'authapp/register.html', context)


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


def send_verify_mail(user):
    verify_link = reverse('auth:verify', args=[user.email,
                                               user.activation_key])
    title = f"Verifying account {user.username}"
    message = (f"To verify your account {user.username}"
               f"at {settings.DOMAIN_NAME} click the link below:"
               f"\n{settings.DOMAIN_NAME}{verify_link}")

    print(f'from: {settings.EMAIL_HOST_USER}, to: {user.email}')
    return send_mail(title, message, settings.EMAIL_HOST_USER, [user.email],
                     fail_silently=False)


def verify(request, email, activation_key):
    try:
        user = ShopUser.objects.get(email=email)
        if user.activation_key == activation_key and not user.is_activation_key_expired():
            print(f'user {user} is activated')
            user.is_active = True
            user.save()
            auth.login(request, user)
            return render(request, 'authapp/verification.html')
        else:
            print(f'error activation user: {user}')
            return render(request, 'authapp/verification.html')

    except Exception as e:
        print(f'error activation user : {e.args}')

    return HttpResponseRedirect(reverse('mainapp:index'))


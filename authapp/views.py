from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib import auth
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView

from authapp.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from basketapp.models import Basket
from .models import User, UserProfile
from django.db import transaction
from authapp.forms import UserProfileEditForm


def send_verify_mail(user):
    verify_link = reverse('auth:verify', args=[user.email, user.activation_key])
    title = f'Активация учетной записи {user.username}'
    messages = f'Для подтверждения учётной записи пройтиде по ссылке: \n{settings.DOMAIN_NAME}' \
               f'{verify_link}'

    return send_mail(title, messages, settings.EMAIL_HOST_USER, [user.email,], fail_silently=False)


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
        else:
            print(form.errors)
    else:
        form = UserLoginForm()
    context = {'form': form,
               'title': 'GeekShop - Авторизация',
               'title_2': 'Авторизация',
               'container_class': 'col-lg-5'
               }
    return render(request, 'authapp/login.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            if send_verify_mail(user):
                messages.success(request, 'Вы успешно зарегистрировались!')
                return HttpResponseRedirect(reverse('auth:login'))
        else:
            print(form.errors)
    else:
        form = UserRegisterForm()
    context = {'form': form,
               'title': 'GeekShop - Регистрация',
               'title_2': 'Регистрация',
               'container_class': 'col-lg-7',
               }
    return render(request, 'authapp/register.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required()
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, files=request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('auth:profile'))
    else:
        form = UserProfileForm(instance=request.user)

    context = {
        'form': form,
        'baskets': Basket.objects.filter(user=request.user),
    }
    return render(request, 'authapp/profile.html', context)


def verify(request, email, activation_key):
    try:
        user = User.objects.get(email=email)
        if user.activation_key == activation_key and not user.is_activation_key_expired():
            user.is_active = True
            user.save()
            auth.login(request, user)
            return render(request, 'authapp/verification.html')
        else:
            print(f'error activation user: {user}')
            return render(request, 'authapp/verification.html')
    except Exception as e:
        print(f'error activation user: {e.args}')
        return HttpResponseRedirect(reverse('main'))


@transaction.atomic
def profile(request):
    title = 'редактирование'

    if request.method == 'POST':
        edit_form = UserProfileForm(data=request.POST, files=request.FILES, instance=request.user)
        profile_form = UserProfileEditForm(data=request.POST, files=request.FILES, instance=request.user.userprofile)

        if edit_form.is_valid() and profile_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('auth:profile'))
    else:
        edit_form = UserProfileForm(data=request.POST, files=request.FILES, instance=request.user)
        profile_form = UserProfileEditForm(data=request.POST, files=request.FILES,
                                               instance=request.user.userprofile)

    context = {
        'title': title,
        'form': edit_form,
        'profile_form': profile_form,
    }
    return render(request, 'authapp/profile.html', context)
















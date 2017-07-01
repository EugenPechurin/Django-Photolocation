# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, redirect, render
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


# @csrf_exempt
def login(request):
    args = {}
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            print('login')
            return JsonResponse ({'answe': 'ok'}) #render(request, 'index.html')
        else:
            args['login_error'] = "Пользователь не найден"
            return JsonResponse ({'answe': 'error'}) #render(request, 'login.html', args)
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    args = {}
    args['form'] = UserCreationForm()
    if request.POST:
        newUser_form = UserCreationForm(request.POST)
        if newUser_form.is_valid():
            newUser_form.save()
            newUser = auth.authenticate(username=newUser_form.cleaned_data['username'], password=newUser_form.cleaned_data['password1'])
            auth.login(request, newUser)
            print('Eeee')
            return redirect('/')
        else:
            args['form'] = newUser_form
    return render(request, 'register.html', args)

from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import copy

from . import models
from . import forms


class BasePerfil(View):
    template_name = 'Profile/_create.html'

    def setup(self, *args, **kwargs) -> None:
        super().setup(*args, **kwargs)
        self.car = copy.deepcopy(self.request.session.get('car',{}))
        self.profile = None

        if self.request.user.is_authenticated:
            self.profile = models.Profile.objects.filter(user=self.request.user).first()

            self.context = {
                'userform': forms.UserForm(
                    data=self.request.POST or None,
                    user=self.request.user,
                    instance=self.request.user),
                'profileform': forms.ProfileForm(
                    data=self.request.POST or None, 
                    instance=self.profile
                )
            }
        else:
            self.context = {
                'userform': forms.UserForm(data=self.request.POST or None),
                'profileform': forms.ProfileForm(data=self.request.POST or None)
            }
        self.userForm = self.context['userform']
        self.profileForm = self.context['profileform']

        if self.request.user.is_authenticated:
            self.template_name = 'Profile/_update.html'
        self.rederizar = render(self.request, self.template_name, self.context)

    def get(self, *args, **kwargs):
        return self.rederizar
    
class Create(BasePerfil):
    def post(self, *args, **kwargs):
        if not self.userForm.is_valid() or not self.profileForm.is_valid():
            messages.error(self.request, 'Existem erros no formulário de cadastro')
            return self.rederizar
        
        username = self.userForm.cleaned_data.get('username')
        password = self.userForm.cleaned_data.get('password')
        email = self.userForm.cleaned_data.get('email')
        first_name = self.userForm.cleaned_data.get('first_name')
        last_name = self.userForm.cleaned_data.get('last_name')

        if self.request.user.is_authenticated:
            user = get_object_or_404(User, username=self.request.user.username)

            user.username = username

            if password:
                user.set_password(password)
            
            user.email = email
            user.first_name = first_name
            user.last_name = last_name
            user.save()

            if not self.profile:
                self.profileForm.cleaned_data['user'] = user
                profile = models.Profile(**self.profileForm.cleaned_data)
                profile.save()
            else:
                profile = self.profileForm.save(commit=False)
                profile.user = user
                profile.save()
        
        else:
            user = self.userForm.save(commit=False)
            user.set_password(password)
            user.save()

            profile = self.profileForm.save(commit=False)
            profile.user = user
            profile.save()

        if password:
            authentic = authenticate(self.request, username=user, password=password)
            if authentic:
                login(self.request, user=user)

            self.request.session['car'] = self.car
            self.request.session.save()

            messages.success(self.request, 'Seu cadastro foi criado ou atualizado com sucesso')

            messages.success(self.request, 'Login realizado com Sucesso')

            return redirect('Product:car')
    
class Update(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Update')

class Login(View):
    def post(self, *args, **kwargs):
        username = self.request.POST.get('username')
        password = self.request.POST.get('password')

        if not username or not password:
            messages.error(self.request, 'Usuário ou senha inválido')
            return redirect('Profile:create')

        user =  authenticate(self.request, username=username, password=password)

        if not user:
            messages.error(self.request, 'Usuário ou senha inválidos')
            return redirect('Profile:create')

        login(self.request, user=username)

        messages.success(self.request, 'Login feito com sucesso')
        return redirect('Product:car')
    
class Logout(View):
    def get(self, *args, **kwargs):
        car = copy.deepcopy(self.request.session.get('car'))

        logout(self.request)
        self.request.session['car'] = car
        self.request.session.save()

        return redirect('Product:list')
    





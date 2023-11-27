
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login, authenticate

from app_perfiles.forms import UserRegisterForm

def registro(request):
   if request.method == "POST":
       formulario = UserRegisterForm(request.POST)

       if formulario.is_valid():
           formulario.save()  
           url_exitosa = reverse('lista_blog')
           return redirect(url_exitosa)
   else:  # GET
       formulario = UserRegisterForm()
   return render(
       request=request,
       template_name='app_perfiles/registro.html',
       context={'form': formulario},
   )

def login_view(request):
   if request.method == "POST":
       form = AuthenticationForm(request, data=request.POST)

       if form.is_valid():
           data = form.cleaned_data
           usuario = data.get('username')
           password = data.get('password')
           user = authenticate(username=usuario, password=password)
           
           if user:
               login(request=request, user=user)
               url_exitosa = reverse('lista_blog')
               return redirect(url_exitosa)
   else:  
       form = AuthenticationForm()
   return render(
       request=request,
       template_name='app_perfiles/login.html',
       context={'form': form},
   )


def inicio(request):
   contexto = {}
   http_response = render(
       request=request,
       template_name='inicio.html',
       context=contexto,
   )
   return http_response
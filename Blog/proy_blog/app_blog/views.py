

# Create your views here.
from django.http import HttpResponse
from datetime import datetime, date
from django.db.models import Q
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from app_blog.models import Articulo
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

def lista_blog(request):
   contexto = {
       "blogs": Articulo.objects.all(),
   }
   http_response = render(
       request=request,
       template_name='lista_blog.html',
       context=contexto,
   )
   return http_response

@login_required
def crear_blog(request):
 
   if request.method == "POST":
       data = request.POST
       act = Articulo(titulo=data['titulo'], subtitulo=data['subtitulo'], cuerpo=data['cuerpo'], autor=data['autor'], fecha=data['fecha'])
       act.save()
       url_exitosa = reverse('lista_blog')
       return redirect(url_exitosa)
   else:  
       return render(
           request=request,
           template_name='crear_blog.html',
       )
   

def eliminar_blog(request, id):
   articulo = Articulo.objects.get(id=id)
   if request.method == "POST":
       articulo.delete()
       url_exitosa = reverse('lista_blog')
       return redirect(url_exitosa)
   
class ArticuloDetailView(DetailView):
    model = Articulo
    success_url = reverse_lazy('lista_blog')
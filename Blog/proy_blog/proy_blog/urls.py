from django.contrib import admin
from django.urls import path
from app_blog.views import lista_blog, crear_blog, eliminar_blog, ArticuloDetailView
from app_perfiles.views import registro, login_view, inicio


urlpatterns = [
    path('admin/', admin.site.urls),
    path('lista-blog/',lista_blog, name= "lista_blog"),
    path("crear-blog/", crear_blog, name= "crear_blog"),
    path('eliminar-blog/<int:id>/', eliminar_blog, name="eliminar_blog"),
    path("articulo-detail/<int:pk>/", ArticuloDetailView.as_view(), name="articulo_detail"),
    path('registro/', registro, name="registro"),
    path('login/', login_view, name="login"),
    path('inicio/', inicio, name= "pagina_inicio")
]

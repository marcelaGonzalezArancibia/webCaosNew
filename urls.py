from django.contrib import admin
from django.urls import path
from .views import  *

urlpatterns = [
    path('', index, name='INDEX'),
    path('galeria/', galeria, name='GALERIA'),
    path('iniciar_sesion/', login, name='LOGIN'),
    path('registrate/', formulario, name='FORMULARIO'),
    path('contacto/', contacto, name='CONTACTO'),

    path('ingresar_noticia/', ingresar_noticia, name='INGRESAR_NOTICIA'),
    path('pagina_noticias/<id>/',pagina_noticias, name='PAGINA_NOTICIAS'),
    
    path('galery/<id>/',galery,name='GALERY'),
   
    path('logout_vista/',logout_vita,name='LOGOUT'),
    path('filtro_desc/',filtro_descripcion,name='FILTRO_DESC'),
    path('filtro_cate/',filtro_cate,name='FILTRO_CATE'),
    path('buscar_notic/',buscar_noticia,name='BUSCAR_NOTIC'),
    path('eliminar/<id>/',eliminar,name='ELIMINAR'),
    path('modificar/<int:noticia_id>/', modificar_noticia, name='MODIFICAR_NOTICIA'),
    path('grabar_galeria/',grabar_galeria,name='GRABAR_GALERIA'),
    path('market/', market, name='MARKET'),

    path('agregar_carrito/<id_articulo>/',agregar_carrito,name='AC'),
    path('quitar/<id_articulo>/',quitar_articulo,name='QA'),
    path('vaciar/',vaciar,name='VACIAR'),
    path('eliminar_arti/<id_articulo>/',eliminar_arti,name='ELIM'),

    
]

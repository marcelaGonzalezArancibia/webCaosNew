from django.contrib import admin
from .models import*
#(registrar models) ver tablas de admin que se crearon en el models.py.

class administracion(admin.ModelAdmin):
    list_display=['idnoticia','nombre_periodista','categoria','foto']
    search_fields=['idnoticia','nombre_periodista']
    list_filter=['categoria']
    list_per_page=3
     
admin.site.register(Categoria)
admin.site.register(Noticia,administracion)
admin.site.register(Galeria)
admin.site.register(objcarrito)


from django.db import models
from django.contrib.auth.models import User
# tablas para pagina del admin.

class Categoria(models.Model):
    categoria=models.CharField(primary_key=True,max_length=60)
    
    def __str__(self) -> str:
        return self.categoria
        
        

        
class Noticia(models.Model):
    idnoticia=models.IntegerField(primary_key=True)
    nombre_periodista=models.CharField(max_length=60)
    titulo_noticia=models.TextField()
    titular_noticia=models.TextField()
    cuerpo_noticia=models.TextField()
    foto=models.ImageField(upload_to='fotos',null=True,default='fotos/defaut.png')
    categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE)
    publicar=models.BooleanField(default=False)
    comentario=models.TextField(default='S/C')
    usuario=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    precio=models.IntegerField(default=100)

    def __str__(self) -> str:
        return self.nombre_periodista

   
class Galeria(models.Model):
    idGaleria= models.AutoField(primary_key=True)
    foto = models.ImageField(upload_to='fotos')
    noticia = models.ForeignKey(Noticia,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return "N°"+str(self.idGaleria)+" /  "+self.noticia.nombre_periodista
    

class objcarrito(models.Model):
    idobjeto = models.AutoField(primary_key=True)
    nombre_objeto = models.CharField(max_length=60)
    precio = models.IntegerField()
    foto = models.ImageField(upload_to='fotos',null=True,default='fotos/default.png')
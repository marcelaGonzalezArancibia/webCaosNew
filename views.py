from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .Carrito import *
# esto es una prueba

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login as login_autent
from django.contrib.auth.decorators import login_required,permission_required

from django.urls import reverse
# Crear los controladores para visualizar las paginas web 
# este metodo para decibir y construir(dibujar) la pagina
#request:me permite enviar y resivir datos de la pagina web
#render:retorna la pagina construida

def logout_vita(request):
    logout(request)
    categorias = Categoria.objects.all()
    noticia=Noticia.objects.all().order_by("-titular_noticia")[:3]
    print(noticia)
    contexto={'categorias':categorias,'noticias':noticia}
    return render(request,"index.html",contexto)
   

def index (request):
    categorias = Categoria.objects.all()
    noticia=Noticia.objects.all().order_by("-titular_noticia")[:3]
    print(noticia)
    contexto={'categorias':categorias,'noticias':noticia}
    return render(request,"index.html",contexto)


def galeria(request):
    noticias=Noticia.objects.all()
    categorias = Categoria.objects.all()
    contar = Noticia.objects.all().count()
    if request.POST:
        nom = request.POST.get("txtBuscar")
        noticias= Noticia.objects.filter(nombre=nom)
        contar = Noticia.objects.filter(nombre=nom).count()
        
    contexto={ 'noticia':noticias,'cantidad':contar,'categorias':categorias}
    return render(request,"galeria.html",contexto)
  
def buscar_noticia(request):
    categorias = Categoria.objects.all()
    desc = request.POST.get("txtBuscar")
    print(desc)
    notic = Noticia.objects.filter(titulo_noticia__contains=desc)
    contar = Noticia.objects.filter(titulo_noticia__contains=desc).count()
    print(contar)
    contexto={'noticia':notic,'cantidad':contar,'categorias':categorias}
    return render(request,"galeria.html",contexto)


def filtro_descripcion(request):
    categorias = Categoria.objects.all()
    desc = request.POST.get("txtDesc")
    print(desc)
    notic = Noticia.objects.filter(nombre_periodista__contains=desc)
    print(notic)
    contar = Noticia.objects.filter(nombre_periodista__contains=desc).count()
    print(contar)
    contexto={'noticia':notic,'cantidad':contar,'categorias':categorias}
    return render(request,"galeria.html",contexto)

def filtro_cate(request):
    cate = request.POST.get("cboCategoria")
    print(cate)
    categorias = Categoria.objects.all()
    if cate=='Todos':
        print("todos pasados")
        notic= Noticia.objects.all()
        contar = Noticia.objects.all().count()
        print(notic)
        print(contar)
    else:
        obj_cate = Categoria.objects.get(categoria=cate)
       
        notic = Noticia.objects.filter(categoria=obj_cate)
        print(notic)
        contar = Noticia.objects.filter(categoria=obj_cate).count()
    
    contexto={'noticia':notic,'cantidad':contar,'categorias':categorias}
    return render(request,"galeria.html",contexto) 
   


def login(request):
    if request.POST:
        usuario = request.POST.get("nombre")
        password = request.POST.get("password")
        us = authenticate(request,username=usuario,password=password)
        if us is not None and us.is_active:
            login_autent(request,us)
            categorias = Categoria.objects.all()
            noticia=Noticia.objects.all().order_by("-titular_noticia")[:3]
            print(noticia)
            contexto={'categorias':categorias,'noticias':noticia}
            return render(request,"index.html",contexto)     
        else:
            return render(request,"login.html",{'msg':'usuario / contraseña invalidos'})
    return render(request,"login.html")

def formulario(request):
    if request.POST:
        nombre = request.POST.get("nombre")
        correo = request.POST.get("email")
        usuario = request.POST.get("username")
        password = request.POST.get("pass")
        confirm_password = request.POST.get("passConfirma")
        try:
             u = User.objects.get(username=usuario)
             mensaje="Usuario ya existe"
             return render(request,'formulario.html',{'msg':mensaje})
        except:
            if password != confirm_password:
                mensaje="contraseñas icorrectas"
                return render(request,'formulario.html',{'msg':mensaje})
            u = User()
            u.first_name=nombre
            u.username=usuario
            u.email=correo
            u.set_password(password)
            u.save()
            us = authenticate(request,username=usuario,password=password)
            login_autent(request,us)
            return render(request,'index.html',{'user':us})
    return render(request,"formulario.html")



def contacto(request):
    return render(request,"contacto.html")




@login_required(login_url='/login/')
def ingresar_noticia(request):
    noticias = Noticia.objects.all()
    categorias = Categoria.objects.all()
    print(request.user.username)
    nom_user=request.user.username
    usu=User.objects.get(username=nom_user)
    print(usu)
    noticia= Noticia.objects.filter(usuario=usu)
    
    if request.method == 'POST':
        accion = request.POST.get("accion")

        if accion == "actualizar":
            id = request.POST.get("txtid")
            nombre_periodista = request.POST.get("txtnombre_periodista")
            titulo = request.POST.get("txttitulo_noticia")
            titular = request.POST.get("txttitular_noticia")
            cuerpo = request.POST.get("txtcuerpo_noticia")
            img = request.FILES.get("txtimg")
            cat = request.POST.get("cbocategoria")
            obj_cate = Categoria.objects.get(categoria=cat)

            try:
                noti = Noticia.objects.get(idnoticia=id)
                noti.nombre_periodista = nombre_periodista
                noti.titulo_noticia = titulo
                noti.titular_noticia = titular
                noti.cuerpo_noticia = cuerpo
                if img is not None:
                    noti.foto = img
                noti.categoria = obj_cate
                noti.save()
                mensaje = "Noticia modificada"
            except Noticia.DoesNotExist:
                mensaje = "No se encontró la noticia"

            return render(request, 'ingresar_noticia.html', {'noticias': noticias, 'mensaje': mensaje, 'categorias': categorias,'noticia': noticia})

        if accion == "eliminar":
            id = request.POST.get("txtid")
            try:
                noti = Noticia.objects.get(idnoticia=id)
                noti.delete()
                mensaje = "Se eliminó la noticia correctamente."
            except Noticia.DoesNotExist:
                mensaje = "No se encontró la noticia."
            noticias = Noticia.objects.all()
            return render(request, 'ingresar_noticia.html', {'noticias': noticias, 'mensaje': mensaje})

        if accion == "enviar":
            id = request.POST.get("txtid")
            nombre_periodista = request.POST.get("txtnombre_periodista")
            titulo = request.POST.get("txttitulo_noticia")
            titular = request.POST.get("txttitular_noticia")
            cuerpo = request.POST.get("txtcuerpo_noticia")
            img = request.FILES.get("txtimg")
            cat = request.POST.get("cbocategoria")
            obj_cate = Categoria.objects.get(categoria=cat)

            noti = Noticia(
                idnoticia=id,
                nombre_periodista=nombre_periodista,
                titulo_noticia=titulo,
                titular_noticia=titular,
                cuerpo_noticia=cuerpo,
                categoria=obj_cate
            )
            if img is not None:
                noti.foto = img
            noti.save()
            mensaje = "Noticia Registrada"
            noticias = Noticia.objects.all()
            return render(request, 'ingresar_noticia.html', {'noticias': noticias, 'mensaje': mensaje})

    return render(request, 'ingresar_noticia.html',{'noticias': noticias, 'categorias': categorias} )

def grabar_galeria(request):
    if request.POST:
        id=request.POST.get("txtId")
        foto=request.FILES.get("txtFoto")
        noticia=Noticia.objects.get(idnoticia=id)
        gale=Galeria(
            foto=foto,
            noticia=noticia
        )
        gale.save()
    return redirect("/ingresar_noticia/")

def pagina_noticias(request,id):
   noticia=Noticia.objects.get(idnoticia=id)
   galeria=Galeria.objects.filter(noticia=noticia)
   data={'noticia':noticia,'galeria':galeria}
   return render(request,"pagina_noticias.html",data)

@login_required(login_url='/login/')
@permission_required('myNoticia.view_noti',login_url='/login/')
@permission_required('myNoticia.delete_noti',login_url='/login/')
def eliminar(request, id):
    try:
        noti = Noticia.objects.get(idnoticia=id)
        noti.delete()
        msg = 'Noticia Eliminada'
    except:
        msg = 'Noticia No Eliminada'
    
    return redirect('INGRESAR_NOTICIA')



def galery(request,id):
    noticia=Noticia.objects.get(idnoticia=id)
    galeria=Galeria.objects.filter(noticia=noticia)
    data={'noticia':noticia,'galeria':galeria}
    return render(request,"galery.html",data)
    
@permission_required('myNoticia.change_noti',login_url='/login/')
def modificar_noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, idnoticia=noticia_id)
    categorias = Categoria.objects.all()
    noticias = Noticia.objects.all()

    if request.method == 'POST':
        # Obtener los datos enviados en el formulario de modificación
        titulo = request.POST.get('txttitulo_noticia')
        titular = request.POST.get('txttitular_noticia')
        cuerpo = request.POST.get('txtcuerpo_noticia')
        categoria = request.POST.get('cbocategoria')

        # Actualizar los datos de la noticia con los valores recibidos
        noticia.titulo_noticia = titulo
        noticia.titular_noticia = titular
        noticia.cuerpo_noticia = cuerpo
        noticia.categoria = categoria
        # Guardar los cambios en la noticia
        noticia.save()

        # Redirigir a la página de listado de noticias o a otra URL
        return redirect('INGRESAR_NOTICIA')

    # Pasar los datos de la noticia al contexto del formulario de modificación
    context = {
        'noticia': noticia,
        'categorias': categorias,
        'noticias': noticias,
        # Otras variables de contexto que necesites
    }
    return render(request, 'ingresar_noticia.html', context)

###########################################################################################################

def agregar_carrito(request, id_articulo):
    carrito = Carrito(request)
    obj = objcarrito.objects.get(idobjeto = id_articulo)
    carrito.agregar(obj)
    datos= request.session["carrito"]
    print(datos)
    return redirect('/market/')

def quitar_articulo(request, id_articulo):
    carrito = Carrito(request)
    obj = objcarrito.objects.get(idobjeto = id_articulo)
    carrito.quitar(obj)
    return redirect('/market/')

def vaciar(request):
    carrito = Carrito(request)
    carrito.vaciar()
    return redirect('/market/')

def eliminar_arti(request,id_articulo):
    carrito = Carrito(request)
    obj = objcarrito.objects.get(idobjeto = id_articulo)
    carrito.eliminar(obj)
    return redirect('/market/')

def market(request):
    productos = objcarrito.objects.all()
    contexto = {'productos': productos}
    print(productos)
    return render(request,"market.html", contexto)





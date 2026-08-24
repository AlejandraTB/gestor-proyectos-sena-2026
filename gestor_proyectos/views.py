from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Proyecto, Tarea


def home(request):
    return render(request, 'home.html')


def mostrar_proyectos(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'proyectos.html', {'proyectos': proyectos})

def nuevos_registros(request):
    proyectos = [
        Proyecto (nombre="Aplicacion de biblioteca", descripcion= "Aplicacion web para gestionar los libros y prestamos de la biblioteca", duarcion = 200),
        Proyecto (nombre="Aplicacion de mensajeria", descripcion= "Aplicacion web para enviar mensajes de texto", duarcion = 1000),
        Proyecto (nombre="Tienda virtual", descripcion= "Aplicacion web para comprar y vender productos en linea", duarcion = 200),]

    for p in proyectos:
        p.save()

    return HttpResponse("Registros guardados")

def ver_proyecto(request, id):
    proyecto= Proyecto.objects.get(id=id)
    return render(request, 'detalle-proyecto.html', {'proyecto': proyecto})
    
'''
** En SQL **

INSER INTO proyecto (nombre, descripcion, duracion) VALUES
("Aplicacion de biblioteca", "Aplicacion web para gestionar los libros y prestamos de la biblioteca,200)''' 


def nuevo_proyecto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        duarcion = request.POST.get('duarcion')

        if nombre and descripcion and duarcion:
            proyecto = Proyecto(
            nombre = nombre,
            descripcion = descripcion,
            duarcion = int(duarcion)
        )
        proyecto.save()

        return redirect('proyectos')
    
    return render(request, 'nuevo-proyecto.html')

def eliminar_proyecto(request, id):
    proyecto = Proyecto.objects.get(id= id )
    proyecto.delete()
    return redirect('proyectos')

def editar_proyecto(request, id):
    proyecto = Proyecto.objects.get(id= id )

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        duarcion = request.POST.get('duarcion')

        if nombre and descripcion and duarcion:
            proyecto.nombre= nombre
            proyecto.descripcion= descripcion
            proyecto.duarcion= int(duarcion)
            proyecto.save()

            return redirect('ver_proyecto', id=proyecto.id)        

    return render (request, 'editar-proyecto.html', {'proyecto': proyecto})

def crear_tarea(request, proyecto_id):
    proyecto = Proyecto.objects.get(id= proyecto_id)

    if request.method == 'POST':
        pass

    datos= {
        'proyecto': proyecto,
        'prioridad_choices': Tarea.PRIORIDAD_CHOICES,
        'estado_choices': Tarea.ESTADO_CHOICES
    }

    return render(request, 'crear-tarea.html', datos)
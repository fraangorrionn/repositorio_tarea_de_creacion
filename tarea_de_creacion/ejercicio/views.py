from django.shortcuts import render
from django.db.models import F
from .models import (
    Usuario,Proyecto,Tarea,
    AsignacionTarea,Etiqueta,Comentario
)


def index(request):
    return render(request, 'index.html') 

def dame_proyecto(request):
    proyecto = Proyecto.objects.select_related("creador").prefetch_related("colaboradores")
    proyecto = proyecto.all()

    return render(request, 'Proyecto/proyecto.html',{"dame_proyecto":proyecto})

def tareas_por_proyecto(request, proyecto_id):
    tareas = Tarea.objects.filter(proyecto=proyecto_id).select_related("proyecto").order_by('-fecha_creacion').all()
    return render(request, 'Proyecto/tarea_por_proyecto.html', {'tareas': tareas})

def asignacion_tarea(request, tarea_id):
    asignaciontarea = AsignacionTarea.objects.filter(tarea = tarea_id).select_related("usuario").select_related("tarea").order_by('fecha_asignacion').all()
    return render(request, 'Asignacion/asignacion_tarea.html', {'asignaciontarea': asignaciontarea})

def texto_observaciones(request,texto_observaciones):
    asignaciontarea = AsignacionTarea.objects.filter(observaciones__icontains = texto_observaciones).select_related("tarea").select_related("usuario").all()
    return render(request, 'Asignacion/texto_observacion.html', {'asignaciontarea': asignaciontarea})

def tareas_completadas(request,fecha_inicio,fecha_final):
    tareas = Tarea.objects.filter(estado = "Co",
                                 fecha_creacion__year__gte = fecha_inicio,
                                 fecha_creacion__year__lte = fecha_final).select_related("proyecto").all()
    return render(request, 'Tarea/tareas_completadas.html', {'tareas': tareas})

def usuario_comentario(request,proyecto_id):
    usuario = Usuario.objects.filter(comentarios_creador__tarea__proyecto=proyecto_id).order_by("-comentarios_creador__fecha_comentario")[:1].get()

    return render(request, 'usuario/usuario_comentario.html', {'usuario': usuario})

def comentarios_palabra_y_ano(request, tarea_id, palabra, ano):
    comentarios = Comentario.objects.filter(
        tarea_id = tarea_id,
        contenido__istartswith=palabra,
        fecha_comentario__year=ano
    ).select_related("autor").all()
    
    return render(request, 'Comentario/comentarios_palabra_y_ano.html', {'comentarios': comentarios})

def etiquetas_por_proyecto(request, proyecto_id):
    etiquetas = Etiqueta.objects.filter(
        tarea__proyecto_id=proyecto_id
    ).distinct()
    
    return render(request, 'Etiqueta/etiquetas_por_proyecto.html', {'etiquetas': etiquetas})

def usuarios_no_asignados(request):
    usuarios = Usuario.objects.exclude(colaboradores_tarea__isnull=False).all()
    return render(request, 'usuario/usuarios_no_asignados.html', {'usuarios': usuarios})


from django.shortcuts import render

def handler_404(request, exception):
    return render(request, '404.html', status=404)

def handler_500(request):
    return render(request, '500.html', status=500)

def handler_403(request, exception):
    return render(request, '403.html', status=403)

def handler_400(request, exception):
    return render(request, '400.html', status=400)
from django.contrib import admin
from .models import Usuario,Proyecto,Tarea,AsignacionTarea,Etiqueta,Comentario

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Proyecto)
admin.site.register(Tarea)
admin.site.register(AsignacionTarea)
admin.site.register(Etiqueta)
admin.site.register(Comentario)
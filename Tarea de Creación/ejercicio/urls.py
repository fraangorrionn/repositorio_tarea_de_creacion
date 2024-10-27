from django.urls import path
from django.conf.urls import handler404, handler500, handler403, handler400

from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path("proyecto/", views.dame_proyecto,name="dame_proyecto"),
    path('proyectos/<int:proyecto_id>/tareas/', views.tareas_por_proyecto, name='tareas_por_proyecto'),
    path('usuario/tareas/', views.tareas_por_proyecto, name='tareas_por_proyecto'),
    path('asignaciones/<int:tarea_id>/', views.asignacion_tarea, name='asignacion_tarea'),
    path("asignaciones/<str:texto_observaciones>/tarea", views.texto_observaciones,name="texto_observaciones"),
    path("tarea/proyecto/<int:fecha_inicio>/<int:fecha_final>", views.tareas_completadas,name="tareas_completadas"),
    path('tarea/<int:tarea_id>/comentarios/<str:palabra>/<int:ano>/', views.comentarios_palabra_y_ano, name='comentarios_palabra_y_ano'),
    path('proyecto/<int:proyecto_id>/etiquetas/', views.etiquetas_por_proyecto, name='etiquetas_por_proyecto'),
    path('usuarios/no-asignados/', views.usuarios_no_asignados, name='usuarios_no_asignados'),

]


handler404 = 'ejercicio.views.handler_404'
handler500 = 'ejercicio.views.handler_500'
handler403 = 'ejercicio.views.handler_403'
handler400 = 'ejercicio.views.handler_400'
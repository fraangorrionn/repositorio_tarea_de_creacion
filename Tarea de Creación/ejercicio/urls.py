from django.urls import path,re_path
from .import views


urlpatterns = [
    path('', views.index, name='index'),
    path("proyecto/", views.dame_proyecto, name="dame_proyecto"),
    path('proyectos/<int:proyecto_id>/tareas/', views.tareas_por_proyecto, name='tareas_por_proyecto'),
    path('usuario/tareas/', views.tareas_por_proyecto, name='tareas_por_proyecto'),
    path('asignaciones/<int:tarea_id>/', views.asignacion_tarea, name='asignacion_tarea'),
    path("asignaciones/observaciones/<str:texto_observaciones>/", views.texto_observaciones, name="texto_observaciones"),
    path('tareas/completadas/<int:ano1>/<int:ano2>/', views.tareas_completadas, name='tareas_completadas'),
]
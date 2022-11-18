from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.form_empleado,name="insertar_empleado"),
    path('<int:id>/',views.form_empleado,name="actualizar_empleado"),
    path('delete/<int:id>/',views.eliminar_empleado,name="eliminar_empleado"),
    path("lista/",views.lista_empleado,name="lista_empleado"),
    
]

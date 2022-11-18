from django.conf import settings
import time
from registrar.models import Empleado

def delete_data():
    hours = time.strftime("%H:%M",time.localtime())
    if hours == "17:18":    
        empleado = Empleado.objects.all()
        empleado.delete()
    else:
        pass

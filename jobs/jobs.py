from django.conf import settings
from django.utils.timezone import now
from datetime import datetime
from registrar.models import Empleado

def delete_data():    
    try:        
        conv = str(now()).split(".")[0]
        expir = conv[0:16]        
        data = Empleado.objects.filter(end_time=expir)
        data.delete()
        
    except Empleado.DoesNotExist as e:
        print(e)
    except Exception as ex:
        print(e)
    


    
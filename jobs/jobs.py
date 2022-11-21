from django.conf import settings
from datetime import datetime
from registrar.models import Empleado

def delete_data():    
    try:
        aa = datetime.now()
        asd = str(aa).split(".")[0]
        xd = asd[0:16]
        data = Empleado.objects.filter(end_time=xd)
        data.delete()
        
    except Empleado.DoesNotExist as e:
        print(e)
        
    


    
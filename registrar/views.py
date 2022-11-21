from django.shortcuts import render,redirect
from background_task import background

import time
from .form import EmpleadosForm
from .models import Empleado
# Create your views here.

def lista_empleado(request):
    context = {'lista_empleado': Empleado.objects.all()}
    return render(request,'register/lista.html',context)
def form_empleado(request,id=0):
    if request.method == 'GET':
        if id==0:
            form = EmpleadosForm()
        else:
            empleado = Empleado.objects.get(pk=id)
            form = EmpleadosForm(instance=empleado)
        return render(request,'register/form.html',{'form':form})
    else:
        if id==0:
            form = EmpleadosForm(request.POST)
        else:
            empleado = Empleado.objects.get(pk=id)
            form = EmpleadosForm(request.POST,instance=empleado)            
            
        if form.is_valid():
            form.save()
        return redirect('/empleado/lista/')    

    
def eliminar_empleado(request,id):
    empleado = Empleado.objects.get(pk=id)
    empleado.delete()
    return redirect('/empleado/lista')


#time.strftime("%m/%d/%Y, %H:%M:%S",time.localtime()


      


       
    
    

        

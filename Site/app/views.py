from urllib import request

from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
from .forms import CreateNewTask
from django.shortcuts import redirect,get_object_or_404

# Create your views here.
def home(request):
    task = Task.objects.all()
    return render (request,'index.html',{
        'task':task
    })

def Create_task(request):
        if request.method == 'GET':  
            return render(request, 'create_task.html',{
            "form": CreateNewTask()
            })
        else:
            Task.objects.create(Product = request.POST['Product'],
            descripcion = request.POST['descripcion'],estado = request.POST['estado']) 
            return redirect('/home/')

def delete_task(request, id):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=id)
        task.delete()
    return redirect('/home/')

def edit_task(request, id):
    task = get_object_or_404(Task, id=id)

    if request.method == 'GET':
        return render(request, 'edit_task.html', {
            'task': task
        })
    else:
        task.Product = request.POST['Product']
        task.descripcion = request.POST['descripcion']
        task.save()
        return redirect('/home/')
    
def ver(request,id):
    task = get_object_or_404(Task,id=id)
    return render(request,'ver.html',{
        'task':task
    })

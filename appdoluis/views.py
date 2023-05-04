from django.shortcuts import render, redirect
from .models import Task

def home(request):
  return render(request, "home.html")

def list_tasks(request):
  tasks = Task.objects.all()
  context = { "tasks": tasks }
  return render(request, "list_tasks.html", context=context)

def create_task(request):
  # Se o usuário submeter o formulário, ele cai no if abaixo
  if request.method == "POST":
    Task.objects.create(
      title=request.POST["title"],
      description=request.POST["description"],
      due_date=request.POST["due-date"],
      done=False
    )
    return redirect("tasks-list")
  
  return render(request, "task_form.html")


def update_task(request,task_id):
  task= Task.objects.get(id=task_id)
  task.due_date= task.due_date.strftime('%Y-%m-%d')
  if request.method == "POST":
    task.title= request.POST["title"],
    task.description=request.POST["description"],
    task.due_date=request.POST["due-date"],
    if 'done' not in request.POST:
      task.done = False
    else:
      task.done= True
    task.done=False
    task.save()
    return redirect("tasks-list")
  
  return render(request,'task_form.html',context= {'task': task })

def delete_task(request,task_id):
  task= Task.objects.get(id= task_id)
  if request.method == 'POST':
    task.delete()
  
  return render(request,'task_form.html')
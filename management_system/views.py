from django.shortcuts import render, redirect
from task.models import Task
from task.forms import TaskForm

def show_task(request):
    data = Task.objects.all()
    print(data)
    return render(request, 'show.html', {'data': data})



def edit_post(request, id):
    post = Task.objects.get(pk=id) 
    post_form = TaskForm(instance=post)

    if request.method == 'POST': 
        post_form = TaskForm(request.POST, instance=post) 
        if post_form.is_valid(): 
            post_form.save() 
            return redirect('show_task')
    return render(request, 'add_task.html', {'form' : post_form})

def delete_post(request, id):
    post = Task.objects.get(pk=id) 
    post.delete()
    return redirect('show_task')
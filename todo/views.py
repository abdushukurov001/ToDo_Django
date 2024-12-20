from django.shortcuts import render,redirect
from .forms import TodoCreateForm
from .models import TodoModel



def todo_list_view(request):
    form = TodoCreateForm()
    # todo = TodoModel.objects.filter(user=request.user)
    todos = request.user.tasks.all()
    show_model = 0
    if request.method == "POST":
        form = TodoCreateForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('todo_list')
        show_model = 1
    return render(request, "todo.html", context={
       'form':form, 
       'todos':todos,
       'show_model': show_model
    })


def todo_create_view(request):
    form = TodoCreateForm()
    return render(request, 'todo_create.html', context={
        'form':form
    } )
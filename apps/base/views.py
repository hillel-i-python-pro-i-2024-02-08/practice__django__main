from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Task
from .forms import TaskForm


def index(request):
    paginator = Paginator(Task.objects.order_by("-date_added"), 6)
    page = request.GET.get('page')

    # tasks = Task.objects.order_by('-date_added')
    try:
        tasks = paginator.get_page(page)
    except EmptyPage:
        tasks = paginator.get_page(1)
    except PageNotAnInteger:
        tasks = paginator.get_page(1)
    except ValueError:
        tasks = paginator.get_page(1)

    context = {"title": "Home", "tasks": tasks, "page_obj": tasks}

    return render(request=request,
                  template_name="index.html",
                  context=context)


def new(request):
    if request.method != "POST":
        # No data was submitted - create an empty form
        form = TaskForm()
    else:
        # Got data from POST-request; Process data
        form = TaskForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("base:index")

    context = {"title": "New", "form": form}
    return render(request=request,
                  template_name="new.html",
                  context=context)


def edit_task(request, task_id):
    if request.method == "POST":
        form = TaskForm(request.POST, instance=Task.objects.get(id=task_id))
        if form.is_valid():
            form.save()
            return redirect('base:index')
    else:
        form = TaskForm(instance=Task.objects.get(id=task_id))
        return render(request=request,
                      template_name='edit_task.html',
                      context={"title": "Edit", "form": form, "task_id": task_id})


def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == "POST":
        task.delete()
        return redirect("base:index")
    else:
        return render(request=request,
                      template_name='delete_task.html',
                      context={"title": "Delete", "task": task}
                      )
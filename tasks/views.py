from django.shortcuts import redirect, render
from django.utils.text import slugify

from tasks.models import Task

from .forms import AddTaskForm


def task_list(request):
    num_tasks = Task.objects.count()
    tasks = Task.objects.all()
    return render(request, './tasks/task_list.html', {'num_tasks': num_tasks, 'tasks': tasks})


def task_detail(request, slug):
    task = Task.objects.get(slug=slug)
    return render(request, 'tasks/task/detail.html', dict(task=task))


def add_task(request):
    if request.method == 'POST':
        if (form := AddTaskForm(request.POST)).is_valid():
            post = form.save(commit=False)
            post.slug = slugify(post.title)
            post.save()
            return redirect('tasks:task-list')
    else:
        form = AddTaskForm()

    return render(request, 'tasks/add_task.html', dict(form=form))


def task_pending(request):
    pass


def task_toggle(request):
    pass


def task_delete(request):
    pass


def task_edit(request):
    pass

from django.shortcuts import redirect, render
from django.utils.text import slugify

from tasks.models import Task

from .forms import AddTaskForm, EditTaskForm


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
            task = form.save(commit=False)
            task.slug = slugify(task.name)
            task.save()
            return redirect('tasks:task-list')
    else:
        form = AddTaskForm()

    return render(request, 'tasks/add_task.html', dict(form=form))


def task_pending(request):
    tasks = Task.objects.all()
    num_tasks_pending = tasks.filter(done=False).count()
    task_pending = tasks.filter(done=False)
    return render(
        request,
        './tasks/task/done_pending.html',
        {'num_pendings': num_tasks_pending, 'task_pending': task_pending},
    )


def task_done(request):
    tasks = Task.objects.all()
    num_tasks_pending = tasks.filter(done=True).count()
    task_pending = tasks.filter(done=True)
    return render(
        request,
        './tasks/task/done_pending.html',
        {'num_pendings': num_tasks_pending, 'task_pending': task_pending},
    )


def task_toggle(request, slug):
    task = Task.objects.get(slug=slug)
    if task.done:
        task.done = False
    else:
        task.done = True
    task.save()
    return redirect('tasks:task-list')


def task_delete(request, slug):
    task = Task.objects.get(slug=slug)
    task.delete()
    return redirect('tasks:task-list')


def task_edit(request, slug: str):
    task = Task.objects.get(slug=slug)

    if request.method == 'POST':
        if (form := EditTaskForm(request.POST, instance=task)).is_valid():
            task = form.save(commit=False)

            task.slug = slugify(task.name)

            task.save()

            return redirect('tasks:task-list')
    else:
        form = EditTaskForm(instance=task)
    return render(request, 'tasks/edit_task.html', dict(tasks=task, form=form))

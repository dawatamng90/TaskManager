from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Task
from .forms import TaskForm
from django.http import JsonResponse

def mark_task_completed(request, id):
    task = get_object_or_404(Task, id=id)

    if request.method == "POST":
        # Set the completed date
        task.completed_date = timezone.now()

        # Use the update_completion_status method
        task.update_completion_status()

        # Return the updated status and completion date
        return JsonResponse({
            'status': task.get_status_display(),
            'completed_date': task.completed_date.strftime("%Y-%m-%d %H:%M:%S")
        })

    return JsonResponse({'error': 'Invalid request method'}, status=400)


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task/task_list.html', {'tasks': tasks})


def task_create_or_edit(request, id=None):
    if id:
        # If id is passed, we are editing an existing task
        task = get_object_or_404(Task, id=id)
        form = TaskForm(request.POST or None, instance=task)
    else:
        # If no id is passed, we are creating a new task
        form = TaskForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()  # Save the task
            return redirect('task_list')  # Redirect to task list after creating/updating
        else:
            print("Form Errors:", form.errors)  # Debugging form errors

    return render(request, 'task/task_create_or_edit.html', {'form': form})


def task_delete(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == "POST":
        task.delete()
        return redirect('task_list')
    return render(request, 'task/task_confirm_delete.html', {'task': task})

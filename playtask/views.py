from django.shortcuts import render
from .forms import ProjectForm
from .forms import TaskForm
from django.contrib.auth.decorators import login_required  # Restrict access to authenticated users


@login_required
def project_list_view(request):
    projects = Project.objects.all()
    no_projects = not projects.exists()  # Check if any projects exist
    context = {'projects': projects, 'no_projects': no_projects}
    return render(request, 'read/project_list.html', context)


@login_required
def project_detail_view(request, pk):
    try:
        project = Project.objects.get(pk=pk)
        tasks = project.task_set.all()
        context = {'project': project, 'tasks': tasks}
    except Project.DoesNotExist:
        context = {'error_message': 'Project not found.'}
    return render(request, 'read/project_detail.html', context)

@login_required
def project_create_view(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new project
        return redirect('project_list')  # Redirect to project list after successful creation
    else:
        form = ProjectForm()  # Create an empty form for GET requests
    context = {'form': form}
    return render(request, 'create/project_create.html', context)


@login_required
def task_create_view(request, pk):
    project = Project.objects.get(pk=pk)  # Get project by ID
    if request.method == 'POST':
        form = TaskForm(request.POST)  # Assuming you have a TaskForm defined (explained later)
        if form.is_valid():
            task = form.save(commit=False)  # Don't save yet
            task.project = project  # Assign the task to the current project
            task.save()  # Now save the task with the project association
from django.shortcuts import redirect
from .models import Project

@login_required
def project_delete_view(request, pk):
    project = Project.objects.get(pk=pk)  # Get the project to be deleted

    if request.method == 'POST':
        project.delete()  # Delete the project object
        return redirect('project_list')  # Redirect to project list after deletion
    else:
        # Display confirmation page (optional)
        context = {'project': project}
        return render(request, 'delete/project_confirm_delete.html', context)  # Optional confirmation template

    # Handle potential errors (e.g., project not found)


@login_required
def project_edit_view(request, pk):
    project = Project.objects.get(pk=pk)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)  # Get form data and populate with project instance
        if form.is_valid():
            project.title = form.cleaned_data['title']  # Update specific fields
            project.description = form.cleaned_data['description']
            project.save()  # Save the updated project instance
            return redirect('project_detail', pk=project.pk)  # Redirect to updated project details
    else:
        form = ProjectForm(instance=project)  # Pre-populate the form with project data
    context = {'project': project, 'form': form}
    return render(request, 'update/project_edit.html', context)


@login_required
def project_confirm_delete_view(request, pk):
    project = Project.objects.get(pk=pk)

    if request.method == 'POST':
        project.delete()
        return redirect('project_list')  # Redirect to project list after deletion
    else:
        context = {'project': project}
        return render(request, 'delete/project_confirm_delete.html', context)
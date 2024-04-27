from django import forms
from .models import Project, Task
from django.shortcuts import render, redirect


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


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task  # Set the model for the form (if using a Task model)
        fields = ['title', 'description']  # Fields to include in the form

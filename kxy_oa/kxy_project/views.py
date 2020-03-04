from django.shortcuts import render
from .models import Project
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,Http404
from django.urls import reverse
from .forms import ProjectForm
def project(request):
    project = Project.objects.order_by('date_added')
    context = {'project':project}
    return render(request,'kxy_project/project.html',context)

@login_required
def my_project(request):
    owner = request.user
    project = Project.objects.filter(owner=owner).order_by('date_added')
    context = {'project':project}
    return render(request,'kxy_project/my_project.html',context)

@login_required
def new_project(request):
    owner = request.user
    if request.method !='POST':
        form = ProjectForm()
    else:
        form = ProjectForm(request.POST)
        if form.is_valid():
            your_new_project = form.save(commit=False)
            your_new_project.owner = request.user
            form.save()
            return HttpResponseRedirect(reverse('kxy_project:my_project'))
    context = {'form':form}
    return render(request,'kxy_project/new_project.html',context)

@login_required
def project_detail(request,project_id):
    project = Project.objects.get(id=project_id)
    context = {'project':project}
    return render(request,'kxy_project/project_detail.html',context)

@login_required
def delete_project(request,project_id):
    project = Project.objects.get(id=project_id)
    if project.owner != request.user:
        return Http404
    Project.objects.get(id=project_id).delete()
    return HttpResponseRedirect(reverse('kxy_project:my_project'))


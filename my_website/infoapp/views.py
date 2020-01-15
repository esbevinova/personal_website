from django.shortcuts import render
from infoapp.models import Project

# Create your views here.
def index(request):
    return render(request, 'infoapp/index.html')

def aboutme(request):
    return render(request, 'infoapp/aboutme.html')

def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'infoapp/myprojects.html', context)

def project_details(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'infoapp/project_detail.html', context)

def resume(request):
    return render(request, 'infoapp/resume.html')

def contactme(request):
    return render(request, 'infoapp/contactme.html')

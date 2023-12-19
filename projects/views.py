from django.shortcuts import render
from projects.models import Project
from django.shortcuts import get_object_or_404

def project_index(request):
    projects = Project.objects.all()
    context = {
        "projects": projects
    }
    return render(request, "projects/project_index.html", context)

def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    template_name = f'projects/project_detail_{project_id}.html'
    return render(request, template_name, {'project': project})

"""
def project_detail(request, project_id):
    project = Project.objects.get(pk=project_id)
    template_name = f'pages/project_detail_{project_id}.html'
    return render(request, template_name, {'project': project})
"""
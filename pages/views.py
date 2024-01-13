from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html', {})

def resume(request):
    return render(request, 'pages/resume.html')


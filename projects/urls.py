# projects/urls.py

from django.urls import path
from projects import views

urlpatterns = [
    path("", views.project_index, name="project_index"),
    path('<int:project_id>/', views.project_detail, name='project_detail'),
]
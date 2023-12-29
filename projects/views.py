from django.shortcuts import render
from projects.models import Project
from django.shortcuts import get_object_or_404
import pandas as pd
import plotly.express as px

####################
# HELPER FUNCTIONS
####################

def u_plot(df):
    fig = px.line(df, 
                  x='stripdate', 
                  y='smoothed_mean', 
                  hover_data={'std'},
                  labels={'stripdate': 'Date', 'smoothed_mean': 'Mean Value', 'std': 'Standard Deviation'})
    fig.update_layout(title='Average Daily Sentiment Score',
                      xaxis_title='Date',
                      yaxis_title='Mean Value',
                      font=dict(family='Andale Mono, monospace', size=12, color='black'),
                      xaxis=dict(showgrid=False),
                      yaxis=dict(showgrid=False),
                      plot_bgcolor='#d7e8f5',
                      paper_bgcolor='#d7e8f5')

    fig.update_traces(
        line=dict(color='#05883b', width=1),
        marker=dict(symbol='circle', size=8, color='red'))

    return fig.to_html(full_html=False)

    
####################
# Main Views
####################

def project_index(request):
    projects = Project.objects.all()
    context = {
        "projects": projects
    }
    return render(request, "projects/project_index.html", context)

def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    template_name = f'projects/project_detail_{project_id}.html'
    
    if project_id == 1:
        df = pd.read_json('projects/static/json/uranium_sentiment_data.json')
        plot_div = u_plot(df)
        context = {'project': project, 'plot_div': plot_div}
    else:
        context = {'project': project}
    return render(request, template_name, context)

"""
def project_detail(request, project_id):
    project = Project.objects.get(pk=project_id)
    template_name = f'pages/project_detail_{project_id}.html'
    return render(request, template_name, {'project': project})
"""
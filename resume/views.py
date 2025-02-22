from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage

#Create your views here.

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")


def projects(request):
    project_show=[
        {
          'title':'NetFlix-Clone',
          'path':'images/netflix.png',
          'link':'https://github.com/Akchauhann/NetFlix-Clone.git'   
        },

        {
            'title':'CRUD Project',
            'path':'images/crudproject.png',
            'link':'https://github.com/Akchauhann/crudproject2.git'
        },
        {
            'title':'Trackip',
            'path':'images/trackip.png',
            'link':'https://github.com/Akchauhann/trackip.git'
        },
        {
            'title':'Recipe-Planner',
            'path':'images/recipe.planner.png',
            'link':'https://github.com/Akchauhann/Recipe-Planner.git'
        },
        
    ]
    return render(request, "projects.html",{"project_show":project_show})

def contact(request):
    return render(request,"contact.html")

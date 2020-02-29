from django.shortcuts import render

def index(request):
    return render(request, 'aula4/index.html')
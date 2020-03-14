from django.shortcuts import render


def index9(request):
    return render(request, "aula9/aula9.html", {"nome":"Camila"})
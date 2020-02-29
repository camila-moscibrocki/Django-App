from django.shortcuts import render


def index(request):
    context = {"alunos": ["Pipoca", "Steven", "Channel", "Chiffon", ]}
    return render(request, 'aula4/index.html', context=context)

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.utils import timezone
from django.conf import settings

def index(request):
    html = f"<h1>Acesso as {timezone.now()} </h1>"
    response = HttpResponse(html, status=404)
    response['ultimo_acesso'] = timezone.now()
    return response

def setacookie(request):
    response = HttpResponse()
    response.set_cookie("my_name", value="(Camila)")

    return response

#def redireciona(request):
#    return HttpResponseRedirect('https://http.cat/')

def cat_status(request, code):
    return HttpResponseRedirect(f'https://http.cat/{code}')

def show_get_values(request):
    import ipdb; ipdb.set_trace()
    nome = "Camila"
    html = f"<h1>Bem vindx {request.GET['nome']}</h1>"
    return HttpResponse(html)
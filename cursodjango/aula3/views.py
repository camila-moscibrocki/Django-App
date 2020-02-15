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

def redireciona(request):
    return HttpResponseRedirect('https://theuselessweb.site/bees/oprahbees.gif')

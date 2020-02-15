from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.utils import timezone
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt

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
    nome = request.GET.get("nome", None)
    if nome is None:
        html = f"<h1>Bem vindx usuário anonimo</h1>"
    else:
        html = f"<h1>Bem vindo {nome} </h1>"
    return HttpResponse(html)

@csrf_exempt
def show_post_values(request):
    head = ""
    if request.method =="POST":
        nome = request.POST.get("nome")
        sobrenome = request.POST.get("sobrenome")
        head += f"<h1> Bem vindo {nome} {sobrenome}</h1>"
    html = """
    <form method =POST>
      <label for="nome">First name:</label><br>
      <input type="text" id="nome" name="nome" value=""><br>
      <label for="sobrenome">Last name:</label><br>
      <input type="text" id="sobrenome" name="sobrenome" value=""><br><br>
      <input type="submit" value="enviar">
    </form>
    """
    html_to_response = head+html
    return HttpResponse(html_to_response)
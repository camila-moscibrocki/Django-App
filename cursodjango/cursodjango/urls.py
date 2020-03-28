from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from aula4.views import index
from aula6.views import index as index6
from aula7.views import index as index7
from aula7.views import restrita, logout_view, permission_view
from aula9.views import index9
from aula10.views import mostra_arquivo_estatico

urlpatterns =[
    path('admin/', admin.site.urls),
    path('', include("aula3.urls")),
    path('estatico', mostra_arquivo_estatico),
    path('aula10', mostra_arquivo_estatico),
    path('aula6', index6),
    path('entrar', index7, name='login'),
    path('aula7/restrita', restrita),
    path('aula7/sair', logout_view, name="logout"),
    path('aula7/view-carrinho', permission_view),
    path('aula9', index9, name="aula9")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.urls import path, include
from . import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    # Quando alguém acessar o site principal (''), chame a função 'pagina_inicial'
    path('', views.pagina_inicial, name='pagina-inicial'),
    path('usuario/', include('usuario.urls')),
    path('ADM/', include('dashboard.urls')),

    # As URLs para seus outros apps (produto, etc.) virão aqui depois
]
from django.urls import path
from . import views

app_name = 'usuario'

urlpatterns = [
    # Quando a URL for /usuario/cadastro/, esta view será chamada
    path('cadastro/', views.cadastro, name="cadastro"),
    
    # Quando a URL for /usuario/login/, esta view será chamada
   path('login/', views.login_user, name="login"),
     # Quando a URL for /usuario/logout/, esta view será chamada
   path('logout/', views.logout_user, name="logout"),
 # Quando a URL for /usuario/perfil/, esta view será chamada
   path('perfil/', views.perfil, name="perfil"),
]
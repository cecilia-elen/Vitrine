from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UsuarioForm, LoginForm

def cadastro(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            # Se estiver tudo certo com o formulário, ele vai salvar e vai fazer login
            usuario = form.save()
            login(request, usuario)
             # Redirecionamento para página inicial
            return redirect(reverse('pagina-inicial')) 
    else:
        form = UsuarioForm()

    context = {'form': form}
    return render(request, 'usuario/cadastro.html', context)

def login_user(request):
     # Se o usuário já está logado, redireciona para a página inicial
    if request.user.is_authenticated:
        return redirect(reverse('pagina-inicial'))
        
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(reverse('pagina-inicial'))
    else:
         # Cria um formulário de login em branco
        form = LoginForm()
 # Envia o formulário (em branco ou com erros) para o template
    context = {'form': form}

    return render(request, 'usuario/login.html', context)

def logout_user(request):
    logout(request)

    return redirect(reverse('pagina-inicial'))
 #Desloga o usuário e o redireciona para a página inicial.

@login_required
def perfil(request):
    """Renderiza a página de perfil do usuário logado."""
    # Rodar o Perfil do usuário com suas informações basiconas
    return render(request, 'usuario/perfil.html')
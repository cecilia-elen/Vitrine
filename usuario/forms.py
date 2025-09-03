from django import forms
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UsuarioForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = ('first_name', 'last_name', 'email', 'cpf')

    # --- Para que o nome do usuário seja colocado ao criar o perfil ---
    def save(self, commit=True):
        # Pega o objeto do usuário criado pelo formulário, mas não salva no banco ainda.
        user = super().save(commit=False)
        # Define o username para ser igual ao email.
        user.username = user.email
        if commit:
            # Agora salva o usuário no banco de dados com o username preenchido.
            user.save()
        return user

class LoginForm(AuthenticationForm):
    pass
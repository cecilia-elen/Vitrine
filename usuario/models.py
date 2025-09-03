from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):

    email = models.EmailField(unique=True)
     # Diz ao Django que o campo de login agora é o 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    cpf = models.CharField(max_length=14,unique=True,verbose_name='CPF',help_text='Informe o CPF no formato 000.000.000-00')

    def __str__(self):
        return self.email # Isso ajuda a ver o email do usuário no painel admin

    class Meta:
        permissions = [
            ('detalha_pessoa', 'Pode ver detalhes de uma pessoa em específico')
        ]

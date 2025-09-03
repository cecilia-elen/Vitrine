# Dentro do arquivo Vitrine/views.py

from django.shortcuts import render

def pagina_inicial(request):
    # Esta função simplesmente diz ao Django para encontrar e mostrar o arquivo 'index.html'
    # Ele vai procurar na pasta templates que configuramos no settings.py
    return render(request, 'index.html')

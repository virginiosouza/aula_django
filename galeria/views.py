from django.shortcuts import render


def index(Request):
    return render(Request, 'galeria\index.html')

def imagem(request):
        return render(request, 'galeria/imagem.html')


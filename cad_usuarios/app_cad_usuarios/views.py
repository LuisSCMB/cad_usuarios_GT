from django.shortcuts import render

def home (request):# request é um parametro no django que te perimite acessar o que esta dentro daquela pagina
    return render (request,'usuarios/home.html')
from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppCoder.models import Curso
from AppCoder.models import UserCreationForm
from django.contrib import messages
from AppCoder.forms import *
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def curso(self):
    curso= Curso(nombre="Python", precio="$3500")
    curso.save()
    documentoDeTexto= f"--->Curso: {curso.nombre}   Precio:  {curso.precio}"

    return HttpResponse(documentoDeTexto)


def register(request):
    form = UserCreationForm()
    return render(request, 'C:\cursos\DjangoPython\Proyecto1\AppCoder\templates\logIn.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'¡Cuenta creada para {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'C:/cursos/DjangoPython/Proyecto1/AppCoder/templates/logIn.html', {'form': form})

def cursoFormulario(request):

    if request.method == "POST":
        curso= Curso (request.POST['curso'], request.POST['camada'])
        curso.save()

        return render(request, "C:/cursos/DjangoPython/Proyecto1/AppCoder/templates/inicio.html")

    return render(request, "C:/cursos/DjangoPython/Proyecto1/AppCoder/templates/cursoFormulario.html")



def logIn(request):
    return render(request, "C:/cursos/DjangoPython/Proyecto1/AppCoder/templates/logIn.html")

def inicio(request):
    return render(request, "C:/cursos/DjangoPython/Proyecto1/AppCoder/templates/inicio.html")

def tienda(request):
    return render(request, "C:/cursos/DjangoPython/Proyecto1/AppCoder/templates/tienda.html")

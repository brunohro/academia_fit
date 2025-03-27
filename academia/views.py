from django.shortcuts import render, redirect
from .models import Personal, Aluno

def index(request): #lista 
    aluno = Aluno.objects.all()
    personal = Personal.objects.all()
    return render(request, "academia/index.html", {"alunos": aluno, "personais": personal})

def cadastro_personal(request): #cadastro
    return render(request, "academia/personal/cadastro_personal.html")

def editar_personal(request, id): #edição
    return render(request, "academia/personal/cadastro_personal.html")

def remover_personal(request, id): #remove
    personal = Personal.objects.get(id=id)
    personal.delete()
    return redirect('index')
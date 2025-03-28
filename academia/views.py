from django.shortcuts import render, redirect
from .models import Personal, Aluno
from .forms import PersonalForm, AlunoForm

def index(request): #lista 
    aluno = Aluno.objects.all()
    personal = Personal.objects.all()
    return render(request, "academia/index.html", {"alunos": aluno, "personais": personal})

def cadastro_personal(request): #cadastro
    if request.method == 'POST':
        form = PersonalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = PersonalForm()
    return render(request, "academia/personal/cadastro_personal.html", {"form": form})

def editar_personal(request, id): #edição
    personal = Personal.objects.get(id=id)
    if request.method == 'POST':
        form = PersonalForm(request.POST, instance=personal)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PersonalForm(instance=personal)
    return render(request, "academia/personal/cadastro_personal.html", {'form': form})

def remover_personal(request, id): #remove
    personal = Personal.objects.get(id=id)
    personal.delete()
    return redirect('index')
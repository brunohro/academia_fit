from django.db import models

from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField()
    idade = models.IntegerField()
    cpf = models.CharField(max_length=11)

    class Meta:
        abstract = True
    
    def __str__(self):
        return self.nome

class Personal(Pessoa):
    especialidade = models.CharField(max_length=100)
    cref = models.CharField(max_length=20, unique=True)

    class Meta:
        verbose_name = "Personal Trainer"
        verbose_name_plural = "Personais Trainers"

class Aluno(Pessoa):
    peso = models.FloatField()
    altura = models.FloatField()
    personal = models.ForeignKey(Personal, on_delete= models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name = "Aluno"
        verbose_name_plural = "Alunos"
        

from uuid import uuid4
from django.db import models

from escola.constants import NIVEL_BAIXO, NIVEL_CURSO, PERIODO_CURSO, PERIODO_MANHA


class Aluno(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(max_length=30, blank=False)
    rg = models.CharField(max_length=9, unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    data_nascimento = models.DateField()
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.nome} - {self.data_nascimento}'


class Curso(models.Model):
    nome = models.CharField(max_length=255)
    codigo_curso = models.UUIDField(default=uuid4, unique=True)
    descricao = models.CharField(max_length=255)
    nivel = models.IntegerField(choices=NIVEL_CURSO, default=NIVEL_CURSO[NIVEL_BAIXO], blank=False, null=False)

    def __str__(self):
        return f'{self.codigo_curso} - {self.nome}'


class Matricula(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo = models.IntegerField(choices=PERIODO_CURSO, blank=False, null=False)

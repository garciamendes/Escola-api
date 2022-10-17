import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from faker import Faker
import random
from escola.models import Curso
from escola.constants import NIVEL_BAIXO, NIVEL_MEDIO, NIVEL_AVANCADO

def criando_cursos(quantidade_de_pessoas):
    fake = Faker('pt_BR')
    Faker.seed(10)

    for _ in range(quantidade_de_pessoas):
        nome = fake.name()
        descricao = 'loren ipsum'
        nivel = random.choice([NIVEL_BAIXO, NIVEL_MEDIO, NIVEL_AVANCADO])
        p = Curso(nome=nome, descricao=descricao, nivel=nivel)
        p.save()

criando_cursos(100)
print('Criado!')
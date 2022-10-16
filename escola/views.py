from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend

from escola.models import Aluno, Curso, Matricula
from escola.serializers import AlunosSerializer
from escola.serializers import CursosSerializer
from escola.serializers import ListaAlunosMatriculaSerializer
from escola.serializers import ListaMatriculasAlunoSerializer
from escola.serializers import MatriculasSerializer


class AlunosViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunosSerializer
    search_fields = ['nome', 'cpf']
    filterset_fields = ['ativo']


class CursosViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursosSerializer


class MatriculasViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculasSerializer


class ListaMatriculasAluno(generics.ListAPIView):
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs.get('pk'))
        return queryset

    serializer_class = ListaMatriculasAlunoSerializer


class ListaAlunosMatricula(generics.ListAPIView):
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs.get('pk'))
        return queryset

    serializer_class = ListaAlunosMatriculaSerializer
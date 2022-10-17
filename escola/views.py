
from rest_framework import viewsets, generics, filters
from rest_framework import status
from rest_framework.response import Response

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

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=status.HTTP_201_CREATED)
            id = str(serializer.data['id'])
            response['Location'] = request.build_absolute_uri() + id
            return response



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
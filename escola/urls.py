from rest_framework import routers

from escola import views

router = routers.DefaultRouter()
router.register(r'alunos', views.AlunosViewSet, basename='alunos')
router.register(r'cursos', views.CursosViewSet, basename='cursos')
router.register(r'matriculas', views.MatriculasViewSet, basename='matriculas')

urlpatterns = router.urls

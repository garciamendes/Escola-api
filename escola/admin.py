from django.contrib import admin

from escola.models import Aluno, Curso, Matricula

class AlunosAdmin(admin.ModelAdmin):
    list_display = ('pk', 'nome', 'rg', 'cpf', 'data_nascimento')
    list_display_links = ('pk', 'nome')
    search_fields = ('nome',)
    list_filter = ('ativo',)
    ordering = ('nome',)
    list_per_page: 5


class CursosAdmin(admin.ModelAdmin):
    list_display = ('pk', 'nome', 'codigo_curso', 'descricao', 'nivel')
    list_display_links = ('pk', 'nome')
    list_filter = ('nivel',)
    search_fields = ('nome',)
    list_per_page: 5

class MatriculaAdmin(admin.ModelAdmin):
    list_display = ('pk', 'aluno', 'curso', 'periodo')
    list_display_links = ('pk', 'aluno')
    list_filter = ('periodo',)
    search_fields = ('curso', 'aluno')
    list_per_page: 5


admin.site.register(Aluno, AlunosAdmin)
admin.site.register(Curso, CursosAdmin)
admin.site.register(Matricula, MatriculaAdmin)

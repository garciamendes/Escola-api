# Generated by Django 4.1.2 on 2022-10-14 19:13

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0002_rename_alunos_aluno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='codigo_curso',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]
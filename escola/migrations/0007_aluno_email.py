# Generated by Django 4.1.2 on 2022-10-15 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0006_aluno_ativo'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='email',
            field=models.EmailField(default='', max_length=30),
        ),
    ]

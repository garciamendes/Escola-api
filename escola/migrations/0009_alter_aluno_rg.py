# Generated by Django 4.1.2 on 2022-10-16 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0008_alter_aluno_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='rg',
            field=models.CharField(max_length=9, unique=True),
        ),
    ]
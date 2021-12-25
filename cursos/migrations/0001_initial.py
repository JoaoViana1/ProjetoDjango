# Generated by Django 3.2.10 on 2021-12-22 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('thumb', models.ImageField(upload_to='thumb_cursos')),
            ],
        ),
        migrations.CreateModel(
            name='Aulas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('aula', models.FileField(upload_to='aulas')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cursos.cursos')),
            ],
        ),
    ]

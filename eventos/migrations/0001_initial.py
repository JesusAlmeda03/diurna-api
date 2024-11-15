# Generated by Django 4.2.16 on 2024-11-13 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Eventos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('poster_url', models.CharField(max_length=200, null=True)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Participantes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('escuela', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=100)),
                ('municipio', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=15)),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventos.eventos')),
            ],
        ),
        migrations.CreateModel(
            name='Tutores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('paterno', models.CharField(max_length=100)),
                ('materno', models.CharField(max_length=100)),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventos.eventos')),
                ('par', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventos.participantes')),
            ],
        ),
        migrations.CreateModel(
            name='Estudiantes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('paterno', models.CharField(default='', max_length=100)),
                ('materno', models.CharField(max_length=100)),
                ('equipo', models.CharField(max_length=100)),
                ('institucion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventos.participantes')),
            ],
        ),
    ]

# Generated by Django 4.1.5 on 2023-02-03 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especie', models.CharField(max_length=40)),
                ('raza', models.CharField(max_length=40)),
                ('peso', models.IntegerField()),
                ('nombre', models.CharField(max_length=30)),
                ('fecha_nacimiento', models.DateField()),
                ('sexo', models.CharField(max_length=20)),
                ('esta_castrado', models.BooleanField()),
                ('direccion', models.CharField(max_length=50)),
                ('dni_tutor', models.CharField(max_length=9)),
                ('descripcion', models.CharField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Profesional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_completo', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('dni', models.CharField(max_length=9)),
                ('especialidad', models.CharField(max_length=40)),
                ('esta_recibido', models.BooleanField()),
                ('esta_activo', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Visita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_visita', models.DateField()),
                ('nombre_paciente', models.CharField(max_length=20)),
                ('nombre_profesional', models.CharField(max_length=50)),
                ('diagnostico', models.CharField(max_length=1000)),
                ('medicacion', models.CharField(blank=True, max_length=500)),
                ('proximo_control', models.DateField(blank=True)),
            ],
        ),
    ]

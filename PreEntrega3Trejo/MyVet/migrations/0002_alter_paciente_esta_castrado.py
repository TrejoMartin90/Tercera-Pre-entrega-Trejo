# Generated by Django 4.1.5 on 2023-02-06 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyVet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='esta_castrado',
            field=models.BooleanField(blank=True),
        ),
    ]

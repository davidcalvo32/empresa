# Generated by Django 4.0 on 2021-12-11 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bienvenido', '0002_empleado_apodo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='nombre',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]

# Generated by Django 4.1 on 2022-09-29 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0003_alter_estudiantes_apellido_alter_estudiantes_nombre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='nombre',
            field=models.CharField(max_length=40),
        ),
    ]
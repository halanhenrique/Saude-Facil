# Generated by Django 3.1.4 on 2020-12-18 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario_paciente', '0003_usuario_paciente_foto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario_paciente',
            name='foto',
        ),
        migrations.DeleteModel(
            name='Profissionais',
        ),
    ]

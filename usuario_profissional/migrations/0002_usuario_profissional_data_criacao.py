# Generated by Django 3.1.4 on 2020-12-02 03:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('usuario_profissional', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario_profissional',
            name='data_criacao',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
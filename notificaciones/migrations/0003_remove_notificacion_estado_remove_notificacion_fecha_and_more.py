# Generated by Django 5.1 on 2024-08-17 07:53

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("notificaciones", "0002_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name="notificacion",
            name="estado",
        ),
        migrations.RemoveField(
            model_name="notificacion",
            name="fecha",
        ),
        migrations.AddField(
            model_name="notificacion",
            name="enviado_en",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="notificacion",
            name="id_usuario",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="notificaciones_generales",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
# Generated by Django 5.0.4 on 2024-05-28 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_cliente_is_empresa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='is_empresa',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
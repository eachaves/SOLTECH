# Generated by Django 5.0.4 on 2024-05-28 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='is_empresa',
            field=models.BooleanField(default=False),
        ),
    ]

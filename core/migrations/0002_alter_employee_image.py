# Generated by Django 4.0.3 on 2022-03-08 14:34

import core.models
from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='image',
            field=stdimage.models.StdImageField(upload_to=core.models.format_file_name, verbose_name='Imagem'),
        ),
    ]

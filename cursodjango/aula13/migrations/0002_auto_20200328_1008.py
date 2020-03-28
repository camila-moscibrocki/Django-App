# Generated by Django 3.0.3 on 2020-03-28 13:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aula13', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfile',
            name='file',
            field=models.ImageField(upload_to='uploads', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg'])]),
        ),
    ]

# Generated by Django 3.0.3 on 2020-03-21 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aula11', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='publicado',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 3.1.5 on 2021-01-08 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotaAtivos', '0010_auto_20210107_2054'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='limInf',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='perfil',
            name='limSup',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]

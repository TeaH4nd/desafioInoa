# Generated by Django 3.1.5 on 2021-01-07 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotaAtivos', '0007_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='email',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
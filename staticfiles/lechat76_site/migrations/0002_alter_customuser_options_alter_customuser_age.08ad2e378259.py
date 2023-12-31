# Generated by Django 4.2.7 on 2023-11-09 15:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lechat76_site', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'Utilisateur', 'verbose_name_plural': 'Utilisateurs'},
        ),
        migrations.AlterField(
            model_name='customuser',
            name='age',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(130)]),
        ),
    ]

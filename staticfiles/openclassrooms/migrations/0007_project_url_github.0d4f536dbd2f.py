# Generated by Django 4.2.7 on 2023-11-10 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openclassrooms', '0006_skill_description_technology_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='url_github',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.1.1 on 2021-03-05 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greenfoot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bonus',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='raceswon',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

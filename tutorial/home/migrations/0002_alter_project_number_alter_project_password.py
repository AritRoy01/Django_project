# Generated by Django 4.2 on 2023-04-19 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='password',
            field=models.IntegerField(),
        ),
    ]

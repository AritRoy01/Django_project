# Generated by Django 4.2 on 2023-04-19 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=20)),
                ('number', models.IntegerField(max_length=10)),
                ('password', models.IntegerField(max_length=20)),
            ],
        ),
    ]

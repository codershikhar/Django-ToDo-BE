# Generated by Django 3.1.1 on 2020-09-29 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='completed',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='todolist',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]

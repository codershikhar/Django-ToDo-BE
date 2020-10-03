# Generated by Django 3.1.1 on 2020-09-30 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('dateTime', models.DateTimeField()),
                ('createdOn', models.DateTimeField(auto_now_add=True)),
                ('updatedOn', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'reminder',
            },
        ),
    ]

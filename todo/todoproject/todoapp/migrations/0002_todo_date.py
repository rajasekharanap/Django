# Generated by Django 4.2 on 2023-05-18 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='date',
            field=models.DateField(default='1999-05-13'),
            preserve_default=False,
        ),
    ]
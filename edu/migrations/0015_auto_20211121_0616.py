# Generated by Django 3.2.9 on 2021-11-21 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0014_auto_20211120_1242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
# Generated by Django 3.2.7 on 2021-11-19 05:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0005_auto_20211119_0456'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='tag',
            new_name='tags',
        ),
    ]

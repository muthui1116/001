# Generated by Django 3.2.9 on 2021-11-20 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0007_auto_20211119_0723'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='images',
            field=models.ImageField(blank=True, upload_to='photos/posts'),
        ),
    ]

# Generated by Django 3.2.9 on 2021-11-20 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0011_auto_20211120_1045'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(blank=True, to='edu.Tag'),
        ),
    ]

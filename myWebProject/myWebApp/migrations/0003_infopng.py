# Generated by Django 5.0.3 on 2024-03-12 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myWebApp', '0002_info_info_info_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfoPng',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media')),
            ],
        ),
    ]

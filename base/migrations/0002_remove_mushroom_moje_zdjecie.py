# Generated by Django 5.0.1 on 2024-03-29 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mushroom',
            name='moje_zdjecie',
        ),
    ]
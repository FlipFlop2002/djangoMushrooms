# Generated by Django 5.0.1 on 2024-03-29 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_remove_mushroom_moje_zdjecie'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mushroom',
            old_name='spec_name',
            new_name='specname',
        ),
    ]
# Generated by Django 5.0.1 on 2024-05-06 17:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0013_course_threshold"),
    ]

    operations = [
        migrations.AddField(
            model_name="coursescore",
            name="passed",
            field=models.BooleanField(default=False),
        ),
    ]

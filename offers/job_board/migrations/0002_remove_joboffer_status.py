# Generated by Django 5.0.3 on 2024-03-10 20:05

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("job_board", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="joboffer",
            name="status",
        ),
    ]

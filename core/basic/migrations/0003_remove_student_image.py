# Generated by Django 4.2.13 on 2024-05-28 13:11

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("basic", "0002_alter_student_email"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="student",
            name="image",
        ),
    ]
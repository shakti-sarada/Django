# Generated by Django 4.2.13 on 2024-06-12 14:11

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("vege", "0004_alter_student_student_address"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="studentid",
            options={"ordering": ["student_id"]},
        ),
    ]

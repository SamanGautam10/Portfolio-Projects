# Generated by Django 5.0.6 on 2024-07-31 13:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0004_studentdetails"),
    ]

    operations = [
        migrations.AlterField(
            model_name="studentdetails",
            name="firstname",
            field=models.TextField(max_length=40),
        ),
        migrations.AlterField(
            model_name="studentdetails",
            name="lastname",
            field=models.TextField(max_length=40),
        ),
    ]

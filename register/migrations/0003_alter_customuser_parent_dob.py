# Generated by Django 5.1.1 on 2024-09-05 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("register", "0002_alter_customuser_child_first_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="parent_dob",
            field=models.DateField(null=True),
        ),
    ]

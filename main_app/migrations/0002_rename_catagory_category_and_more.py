# Generated by Django 4.2.3 on 2023-08-07 22:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main_app", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="catagory",
            new_name="Category",
        ),
        migrations.RenameField(
            model_name="event",
            old_name="catagory",
            new_name="category",
        ),
        migrations.AlterField(
            model_name="event",
            name="participants",
            field=models.IntegerField(),
        ),
    ]
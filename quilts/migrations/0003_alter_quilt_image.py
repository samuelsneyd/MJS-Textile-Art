# Generated by Django 4.1 on 2022-11-05 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quilts", "0002_quilt_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="quilt",
            name="image",
            field=models.ImageField(upload_to="media/"),
        ),
    ]

# Generated by Django 4.1 on 2022-11-05 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quilts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="quilt",
            name="image",
            field=models.CharField(default="", max_length=128),
            preserve_default=False,
        ),
    ]
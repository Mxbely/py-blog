# Generated by Django 4.1 on 2024-11-07 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="commentary",
            options={
                "ordering": ["-created_time"],
                "verbose_name": "Commentary",
                "verbose_name_plural": "Commentaries",
            },
        ),
        migrations.AlterModelOptions(
            name="post",
            options={
                "ordering": ["-created_time"],
                "verbose_name": "Post",
                "verbose_name_plural": "Posts",
            },
        ),
    ]
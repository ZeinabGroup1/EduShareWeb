# Generated by Django 4.2.3 on 2023-07-20 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_blog_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="blog_person_id",
            field=models.IntegerField(),
        ),
    ]

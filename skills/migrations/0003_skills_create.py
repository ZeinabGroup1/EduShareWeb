# Generated by Django 4.2.3 on 2023-07-11 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0002_request'),
    ]

    operations = [
        migrations.AddField(
            model_name='skills',
            name='create',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]

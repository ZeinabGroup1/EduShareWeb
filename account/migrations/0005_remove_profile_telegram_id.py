# Generated by Django 4.2.3 on 2023-07-11 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_messages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='telegram_id',
        ),
    ]

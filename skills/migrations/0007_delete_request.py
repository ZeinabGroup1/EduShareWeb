# Generated by Django 4.2.3 on 2023-07-11 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0006_alter_request_status'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Request',
        ),
    ]

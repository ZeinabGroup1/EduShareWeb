# Generated by Django 4.2.3 on 2023-07-11 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0005_remove_skills_days_delete_weekdays'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='status',
            field=models.CharField(choices=[('accepted', 'accepted'), ('pending', 'pending')], max_length=100),
        ),
    ]
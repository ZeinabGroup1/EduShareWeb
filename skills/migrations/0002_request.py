# Generated by Django 4.2.3 on 2023-07-08 16:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('skills', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('accepted', 'accepted'), ('n_accepted', 'n_accepted'), ('pending', 'pending')], max_length=100)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request_receiver', to=settings.AUTH_USER_MODEL)),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request_skill', to='skills.skills')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

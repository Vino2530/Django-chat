# Generated by Django 3.2.9 on 2021-12-07 03:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('seen', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receive_messages', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('date_created',),
            },
        ),
    ]

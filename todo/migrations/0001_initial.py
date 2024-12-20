# Generated by Django 5.1.4 on 2024-12-11 09:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TodoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('description', models.TextField()),
                ('status', models.BooleanField(default=False)),
                ('cron', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='tasks', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'todo',
                'verbose_name_plural': 'todos',
                'db_table': 'todos',
                'ordering': ['-created_at'],
            },
        ),
    ]
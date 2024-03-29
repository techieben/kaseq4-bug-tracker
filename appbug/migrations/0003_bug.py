# Generated by Django 3.0.6 on 2020-05-22 18:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('appbug', '0002_customuser_display_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('N', 'New'), ('P', 'In Progress'), ('D', 'Done'), ('I', 'Invalid')], default='N', max_length=1)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bug_author', to=settings.AUTH_USER_MODEL)),
                ('closer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bug_closer', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bug_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

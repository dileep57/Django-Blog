# Generated by Django 2.0.1 on 2018-01-16 09:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_postblog_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postblog',
            name='user',
        ),
    ]
# Generated by Django 2.0.1 on 2018-01-09 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180109_1922'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postblog',
            old_name='tit',
            new_name='title',
        ),
    ]
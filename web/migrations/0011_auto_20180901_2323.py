# Generated by Django 2.0.5 on 2018-09-01 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_data_addr'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='addr',
            new_name='file',
        ),
        migrations.RemoveField(
            model_name='data',
            name='data_addr',
        ),
        migrations.RemoveField(
            model_name='data',
            name='size',
        ),
    ]

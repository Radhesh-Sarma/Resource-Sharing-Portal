# Generated by Django 3.1 on 2020-09-21 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_merge_20200310_1815'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='resource_type',
        ),
    ]
# Generated by Django 3.2.8 on 2021-12-28 01:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_journalnotes_notes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journalnotes',
            name='logged_by',
        ),
    ]

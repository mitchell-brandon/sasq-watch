# Generated by Django 3.2.8 on 2021-12-23 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20211221_1906'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='notes',
            field=models.TextField(default=''),
        ),
    ]
# Generated by Django 3.2.8 on 2021-12-27 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_bookmark_special_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='notes',
            field=models.CharField(default='', max_length=5000),
        ),
    ]

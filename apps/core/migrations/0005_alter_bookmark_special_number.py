# Generated by Django 3.2.8 on 2021-12-26 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20211226_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='special_number',
            field=models.IntegerField(default=''),
        ),
    ]

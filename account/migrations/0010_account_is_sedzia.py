# Generated by Django 3.2.9 on 2022-01-06 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_auto_20220106_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='is_sedzia',
            field=models.BooleanField(default=False),
        ),
    ]

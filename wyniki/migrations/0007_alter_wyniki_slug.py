# Generated by Django 3.2.6 on 2021-10-06 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wyniki', '0006_auto_20211006_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wyniki',
            name='slug',
            field=models.SlugField(default=0),
        ),
    ]

# Generated by Django 3.2.9 on 2022-11-15 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_auto_20221115_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='nr_patentu_strzeleckiego',
            field=models.CharField(blank=True, default='None', max_length=30, null=True, verbose_name='Numer patentu strzeleckiego'),
        ),
    ]

# Generated by Django 3.2.9 on 2022-11-15 12:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_account_rodo_accepted'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='adres',
            field=models.TextField(default='0', verbose_name='Adres'),
        ),
        migrations.AddField(
            model_name='account',
            name='cel_czlon_kolekcjonerski',
            field=models.BooleanField(default=False, verbose_name='Cel członkostwa: Kolekcjonerski'),
        ),
        migrations.AddField(
            model_name='account',
            name='cel_czlon_sportowy',
            field=models.BooleanField(default=False, verbose_name='Cel członkostwa: Sportowy'),
        ),
        migrations.AddField(
            model_name='account',
            name='data_urodzenia',
            field=models.DateField(default=datetime.date.today, verbose_name='Data urodzenia'),
        ),
        migrations.AddField(
            model_name='account',
            name='imie_ojca',
            field=models.CharField(default='None', max_length=30, verbose_name='Imię ojca'),
        ),
        migrations.AddField(
            model_name='account',
            name='is_stowarzyszenie_member',
            field=models.BooleanField(default=False, verbose_name='Członek stowarzyszenia'),
        ),
        migrations.AddField(
            model_name='account',
            name='kod_poczowy',
            field=models.IntegerField(default=0, verbose_name='Kod kod_poczowy'),
        ),
        migrations.AddField(
            model_name='account',
            name='miejsce_urodzenia',
            field=models.CharField(default='None', max_length=30, verbose_name='Miejsce urodzenia'),
        ),
        migrations.AddField(
            model_name='account',
            name='miejscowosc',
            field=models.CharField(default='None', max_length=30, verbose_name='Miejscowość'),
        ),
        migrations.AddField(
            model_name='account',
            name='nr_patentu_strzeleckiego',
            field=models.CharField(default='None', max_length=30, verbose_name='Numer patentu strzeleckiego'),
        ),
        migrations.AddField(
            model_name='account',
            name='nr_telefonu',
            field=models.IntegerField(default=0, verbose_name='Numer telefonu'),
        ),
        migrations.AddField(
            model_name='account',
            name='pesel',
            field=models.CharField(default=0, max_length=11, verbose_name='PESEL'),
        ),
        migrations.AddField(
            model_name='account',
            name='pozwolenie_kolekcjonerski',
            field=models.BooleanField(default=False, verbose_name='Posiadam pozwolenie na broń: Kolekcjonerski'),
        ),
        migrations.AddField(
            model_name='account',
            name='pozwolenie_sportowy',
            field=models.BooleanField(default=False, verbose_name='Posiadam pozwolenie na broń: Sportowy'),
        ),
    ]

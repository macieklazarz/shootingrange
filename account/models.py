from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import datetime
from django.shortcuts import render, redirect, reverse
import mainapp
# from mainapp.models import LtsPayment
# from zawody.models import Turniej
# Create your models here.

class MyAccountManager(BaseUserManager):
	def create_user(self, email, username, password=None):
		if not email:
			raise ValueError("Users must have mail address")
		if not username:
			raise ValueError("Users must have mail username")

		user = self.model(
				email=self.normalize_email(email),
				username=username,
			)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, username, password):
		user = self.create_user(
				email=self.normalize_email(email),
				password = password,
				username=username,
			)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user




class Account(AbstractBaseUser):
	email 					= models.EmailField(verbose_name="email", max_length=60, unique=True, null=False)
	username 				= models.CharField(max_length=30, unique=True, verbose_name="Username")
	imie					=models.TextField(max_length=60, null=False, verbose_name="Imię")
	nazwisko				=models.TextField(max_length=60, null=False, verbose_name="Nazwisko")	
	licencja				=models.TextField(max_length=60, verbose_name='Numer licencji', blank=True, null=True)
	licencja_sedziego		=models.TextField(max_length=60, verbose_name='Numer licencji sędziego', blank=True, null=True)
	klub					=models.TextField(max_length=60,  blank=True, null=True, verbose_name="Klub")
	klasa_sedziego			=models.TextField(max_length=60, verbose_name='Klasa sędziego', blank=True, null=True)
	date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
	is_admin				= models.BooleanField(default=False)
	is_active				= models.BooleanField(default=True)
	is_staff				= models.BooleanField(default=False)
	is_superuser			= models.BooleanField(default=False)
	is_sedzia				= models.BooleanField(default=False)
	# paid					= models.BooleanField(default=False)
	rts						= models.BooleanField(default=False)
	rodo_accepted			= models.BooleanField(default=False)

	data_urodzenia 				= models.DateField(default=datetime.date.today, verbose_name='Data urodzenia')
	is_stowarzyszenie_member	= models.BooleanField(default=False, verbose_name='Członek stowarzyszenia')
	pesel						= models.CharField(max_length=11, default=00000000000, verbose_name='PESEL')
	nr_telefonu 				= models.TextField(default='None', verbose_name='Numer telefonu')
	adres 						= models.TextField(default='None', verbose_name='Adres')
	kod_poczowy					= models.TextField(default='None', verbose_name='Kod pocztowy')
	miejscowosc 				= models.CharField(max_length=30, default='None', verbose_name='Miejscowość')
	imie_ojca	 				= models.CharField(max_length=30, default='None', verbose_name='Imię ojca')
	miejsce_urodzenia			= models.CharField(max_length=30, default='None', verbose_name='Miejsce urodzenia')
	cel_czlon_sportowy 			= models.BooleanField(default=False, verbose_name='Cel członkostwa: Sportowy')
	cel_czlon_kolekcjonerski 	= models.BooleanField(default=False, verbose_name='Cel członkostwa: Kolekcjonerski')
	nr_patentu_strzeleckiego 	= models.CharField(max_length=30, default='None', verbose_name='Numer patentu strzeleckiego', blank=True, null=True)
	pozwolenie_kolekcjonerski 	= models.BooleanField(default=False, verbose_name='Posiadam pozwolenie na broń: Kolekcjonerski')
	pozwolenie_sportowy 		= models.BooleanField(default=False, verbose_name='Posiadam pozwolenie na broń: Sportowy')


	# first_name

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username',]

	objects = MyAccountManager();

	def __str__(self):
		return (self.nazwisko+' '+self.imie)

	def get_data(self):
		return {
			'imie': self.imie,
			'nazwisko': self.nazwisko,
			'email': self.email,
			'username': self.username
		}

	def check_payment(self):
		payment = mainapp.models.LtsPayment.objects.filter(user=self, result='success').count()
		if payment>0:
			payment_succesfull = True
		else:
			payment_succesfull = False

		return payment_succesfull


	def has_perm(self, perm, obj=None):
		return self.is_admin

	def has_module_perms(self, app_label):
		return True

	def user_update(self):
		return reverse("BlogUserUpdateAdminView", kwargs={'pk': self.id})

	class Meta:
		verbose_name = 'Użytkownik'



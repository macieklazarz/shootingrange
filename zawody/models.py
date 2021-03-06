from django.db import models
from account.models import Account


class Turniej(models.Model):
	nazwa = models.CharField(max_length=30)
	rejestracja = models.BooleanField(default=True, verbose_name='Rejestracja')
	klasyfikacja_generalna = models.BooleanField(default=True, verbose_name='Klasyfikacja generalna')
	turniej_archiwalny = models.BooleanField(default=False, verbose_name='Turniej archiwalny')
	wyniki_widoczne = models.BooleanField(default=True, verbose_name='Pokaż wyniki')
	wyniki_generalne_widoczne = models.BooleanField(default=True, verbose_name='Pokaż wyniki generalne')

	def __str__(self):
		return self.nazwa

class ZawodyGrupa(models.Model):
	nazwa = models.CharField(max_length=60)

	def __str__(self):
		return self.nazwa

class Zawody(models.Model):
	nazwa = models.CharField(max_length=30)
	liczba_strzalow = models.IntegerField(default=10)
	turniej = models.ForeignKey(Turniej, on_delete=models.CASCADE, null=True, blank=True)
	oplata_konkurencja = models.FloatField(default=0)
	oplata_bron = models.FloatField(default=0)
	oplata_amunicja = models.FloatField(default=0)
	zawody_grupa = models.ForeignKey(ZawodyGrupa, on_delete=models.SET_NULL, null=True, blank=True)

	def __str__(self):
		return self.nazwa
# Create your models here.
	class Meta:
		verbose_name_plural = "Zawody statyczne"



class Sedzia(models.Model):
	zawody 		= models.ForeignKey(Zawody, on_delete=models.CASCADE)
	sedzia 		= models.ForeignKey(Account, on_delete=models.CASCADE)


	class Meta:
		verbose_name_plural = "Sędziowie"





class ZawodyDynamic(models.Model):
	nazwa = models.CharField(max_length=30)
	turniej = models.ForeignKey(Turniej, on_delete=models.CASCADE, null=True, blank=True)
	oplata_konkurencja = models.FloatField(default=0)
	oplata_bron = models.FloatField(default=0)
	oplata_amunicja = models.FloatField(default=0)
	miss = models.IntegerField(default=0)
	procedura = models.IntegerField(default=0)
	noshoot = models.IntegerField(default=0)



	def __str__(self):
		return self.nazwa
# Create your models here.
	class Meta:
		verbose_name_plural = "Zawody dynamiczne"


class SedziaDynamic(models.Model):
	zawody 		= models.ForeignKey(ZawodyDynamic, on_delete=models.CASCADE)
	sedzia 		= models.ForeignKey(Account, on_delete=models.CASCADE)


	class Meta:
		verbose_name_plural = "Sędziowie konkurencji dynamicznych"
from django import forms
from .models import PostComment
from django.contrib.auth.forms import UserCreationForm
from account.models import Account
from django.forms import ModelForm, TextInput, EmailInput, DateInput

class PostCommentForm(forms.ModelForm):
	class Meta:
		model = PostComment
		fields = ('content',)


class BlogRegistrationForm(UserCreationForm):
	# email = forms.EmailField(max_length=60, help_text='Required. Add a valid email address')

	class Meta:
		model = Account
		fields = ("email", "username", "imie", "nazwisko", "data_urodzenia", "pesel","nr_telefonu", "adres", "kod_poczowy", "miejscowosc", "imie_ojca", "miejsce_urodzenia", "licencja_sedziego", "cel_czlon_sportowy",
			  "licencja", "nr_patentu_strzeleckiego", "pozwolenie_sportowy", "cel_czlon_kolekcjonerski", "pozwolenie_kolekcjonerski",  "password1", "password2", "rodo_accepted", "is_stowarzyszenie_member")

	def clean(self):
		#nawisko ma być zapisane wielkimi literami
		cleaned_data = super().clean()
		nazwisko = cleaned_data.get('nazwisko') 
		nazwisko = nazwisko.upper()

		self.cleaned_data['nazwisko'] = nazwisko
		self.cleaned_data['is_stowarzyszenie_member'] = 1
		if self.cleaned_data['rodo_accepted'] != 1:
			raise forms.ValidationError('Musisz zaakceptować postanowienia RODO aby przejść dalej')

	# def __init__(self, *args, **kwargs):
		
	# 	self.fields["imie"] = 'assdadsad@op.pl'
	# 	super(BlogRegistrationForm, self).__init__(*args,**kwargs)

class BlogAccountAdminEdit(forms.ModelForm):

	class Meta:
		model = Account
		fields = ("email", "username", "imie", "nazwisko", "data_urodzenia", "pesel","nr_telefonu", "adres", "kod_poczowy", "miejscowosc", "imie_ojca", "miejsce_urodzenia", "licencja_sedziego", "cel_czlon_sportowy",
			  "licencja", "nr_patentu_strzeleckiego", "pozwolenie_sportowy", "cel_czlon_kolekcjonerski", "pozwolenie_kolekcjonerski", "rodo_accepted", "is_stowarzyszenie_member")
		widgets = {'imie': TextInput(attrs={'class': "form-control",'style': 'max-width: 300px;','placeholder': 'Imię'}), 
		'nazwisko': TextInput(attrs={'class': "form-control",'style': 'max-width: 300px;','placeholder': 'Nazwisko'}),
		'username': TextInput(attrs={'class': "form-control",'style': 'max-width: 300px;','placeholder': 'Username'}),
		'pesel': TextInput(attrs={'class': "form-control",'style': 'max-width: 300px;','placeholder': 'PESEL'}),
		'nr_telefonu': TextInput(attrs={'class': "form-control",'style': 'max-width: 300px;','placeholder': 'Numer telefonu'}),
		'adres': TextInput(attrs={'class': "form-control",'style': 'max-width: 300px;','placeholder': 'Adres'}),
		'kod_poczowy': TextInput(attrs={'class': "form-control",'style': 'max-width: 300px;','placeholder': 'Kod pocztowy'}),
		'miejscowosc': TextInput(attrs={'class': "form-control",'style': 'max-width: 300px;','placeholder': 'Miejscowość'}),
		'imie_ojca': TextInput(attrs={'class': "form-control",'style': 'max-width: 300px;','placeholder': 'Imię ojca'}),
		'miejsce_urodzenia': TextInput(attrs={'class': "form-control",'style': 'max-width: 300px;','placeholder': 'Miejsce urodzenia'}),
		'licencja_sedziego': TextInput(attrs={'class': "form-control",'style': 'max-width: 300px;','placeholder': 'Numer licencji sędziego'}),
		'licencja': TextInput(attrs={'class': "form-control",'style': 'max-width: 300px;','placeholder': 'Numer licencji'}),
		'nr_patentu_strzeleckiego': TextInput(attrs={'class': "form-control",'style': 'max-width: 300px;','placeholder': 'Numer patentu strzeleckiego'}),
		'email': EmailInput(attrs={'class': "form-control",'style': 'max-width: 300px;','placeholder': 'Email'}),
		'data_urodzenia': DateInput(attrs={'class': "form-control",'style': 'max-width: 300px;','placeholder': 'Data urodzenia'})




		}
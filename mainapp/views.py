from django.shortcuts import render, get_object_or_404, reverse, redirect
import random
from zawody.models import Turniej
from .models import Post, PostComment, ForumTopic, ForumPost, ForumComment, LtsPayment
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import PostCommentForm, BlogRegistrationForm, BlogAccountAdminEdit
from shootingrange import settings
import urllib
from urllib.request import urlopen
import json
import urllib.request
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from datetime import datetime
from account.models import Account
from django.http import JsonResponse
from django.views.generic.base import View
import hashlib
from requests.auth import HTTPBasicAuth
import requests
from django.http import HttpResponse, HttpResponseRedirect

def home_screen_view(request, pk):
	context = {}
	context['pk'] = pk
	context['nazwa_turnieju'] = nazwa_turnieju(pk)
	return render(request, "mainapp/home.html", context)

def zarzadzanie(request, pk):
	context = {}
	context['pk'] = pk
	context['nazwa_turnieju'] = nazwa_turnieju(pk)
	if request.user.is_admin or request.user.rts:
		return render(request, "mainapp/zarzadzanie.html", context)
	return redirect('not_authorized')


def nazwa_turnieju(arg):
	nazwa = Turniej.objects.filter(id=arg)
	# print(f'nazwa {nazwa[0].wyniki_widoczne}')
	# nazwa = Turniej.objects.filter(id=arg).values_list('nazwa')
	# nazwa_flat = []
	# for i in nazwa:
	# 	nazwa_flat.append(i)
	# nazwa_str = ''.join(nazwa_flat[0])

	return nazwa


class BlogMainView(ListView):
	# login_url = 'start'
	template_name = "mainapp/blog_main_page.html"
	model = Post
	context_object_name = 'posts'
	ordering = ['-created_on']


class PostDetailView(DetailView):
	model = Post
	template_name = "mainapp/post_detail.html"
	# context_object_name = 'post'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		slug = self.kwargs['slug']
		form = PostCommentForm()

		post = get_object_or_404(Post, slug=slug)
		comments =  PostComment.objects.filter(post=post)

		context['post'] = post
		context['comments'] = comments
		context['form'] = form

		return context

	def post(self, request, *args, **kwargs):
		form = PostCommentForm(request.POST)
		self.object = self.get_object()
		context = super().get_context_data(**kwargs)

		post = Post.objects.filter(slug=self.kwargs['slug'])[0]
		comments = PostComment.objects.filter(post=post)

		context['post'] = post
		context['comments'] = comments
		context['form'] = form

		if form.is_valid() and self.request.user.is_authenticated:
			content = form.cleaned_data['content']
			author = self.request.user

			comment = PostComment.objects.create(content=content, post=post, author=author)

			form = PostCommentForm()
			context['form'] = form
			return self.render_to_response(context=context)

		return self.render_to_response(context=context)



class PostCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
	model = Post
	template_name = "mainapp/post_create.html"
	fields = ['title', 'content', 'image']

	def test_func(self):
		return self.request.user.is_admin == 1

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class ForumListView(ListView):
	template_name = "mainapp/forum.html"
	model = ForumTopic
	context_object_name = 'topics'


class ForumTopicCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
	model = ForumTopic
	template_name = "mainapp/forum_topic_create.html"
	fields = ['topic']

	def test_func(self):
		return self.request.user.is_admin == 1

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def get_success_url(self):
		return reverse('ForumListView')



class ForumPostCreateView(LoginRequiredMixin, CreateView):
	model = ForumPost
	template_name = "mainapp/post_create.html"
	fields = ['topic', 'title', 'content']

	# def test_func(self):
	# 	return self.request.user.is_admin == 1

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def get_success_url(self):
		return reverse('ForumListView')


# class ForumPostDetailView(LoginRequiredMixin, DetailView):
# 	model = ForumPost
# 	template_name = "mainapp/forum_post_detail.html"
# 	context_object_name = 'post'


class ForumPostDetailView(LoginRequiredMixin, DetailView):
	model = ForumPost
	template_name = "mainapp/forum_post_detail.html"
	context_object_name = 'post'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		slug = self.kwargs['slug']
		form = PostCommentForm()

		post = get_object_or_404(ForumPost, slug=slug)
		comments =  ForumComment.objects.filter(post=post)

		context['post'] = post
		context['comments'] = comments
		context['form'] = form

		return context

	def post(self, request, *args, **kwargs):
		form = PostCommentForm(request.POST)
		self.object = self.get_object()
		context = super().get_context_data(**kwargs)

		post = ForumPost.objects.filter(slug=self.kwargs['slug'])[0]
		comments = ForumComment.objects.filter(post=post)

		context['post'] = post
		context['comments'] = comments
		context['form'] = form

		if form.is_valid() and self.request.user.is_authenticated:
			content = form.cleaned_data['content']
			author = self.request.user

			comment = ForumComment.objects.create(content=content, post=post, author=author)

			form = PostCommentForm()
			context['form'] = form
			return self.render_to_response(context=context)

		return self.render_to_response(context=context)



def blog_registration(request):
	context={}
	if request.POST:
		form=BlogRegistrationForm(request.POST)
		if form.is_valid():
			# print('jest is valid')
			recaptcha_response = request.POST.get('g-recaptcha-response')
			url = 'https://www.google.com/recaptcha/api/siteverify'
			values = {'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,'response': recaptcha_response}
			data = urllib.parse.urlencode(values).encode()
			req =  urllib.request.Request(url, data=data)
			response = urllib.request.urlopen(req)
			result = json.loads(response.read().decode())
			if result['success']:
				# print('jest success')
				form.save()
				# messages.success(request, 'New comment added with success!')
				email = form.cleaned_data.get('email')
				raw_password = form.cleaned_data.get('password1')
				account = authenticate(email=email, password=raw_password)
				login(request, account)
				return redirect('BlogMainView')
			else:
				# print(' nie ma success')
				messages.error(request, 'Invalid reCAPTCHA. Please try again.')
		else:
			pre_email = form.cleaned_data.get('email')
			pre_username = form.cleaned_data.get('username')
			pre_imie = form.cleaned_data.get('imie')
			pre_nazwisko = form.cleaned_data.get('nazwisko')
			pre_data_urodzenia = form.cleaned_data.get('data_urodzenia')
			print(pre_data_urodzenia)
			pre_pesel = form.cleaned_data.get('pesel')
			pre_nr_telefonu = form.cleaned_data.get('nr_telefonu')
			pre_adres = form.cleaned_data.get('adres')
			pre_kod_pocztowy = form.cleaned_data.get('kod_poczowy')
			pre_miejscowosc = form.cleaned_data.get('miejscowosc')
			pre_imie_ojca = form.cleaned_data.get('imie_ojca')
			pre_miejsce_urodzenia = form.cleaned_data.get('miejsce_urodzenia')
			# pre_miejsce_urodzenia = form.cleaned_data.get('miejsce_urodzenia')
			pre_licencja = form.cleaned_data.get('licencja')
			pre_nr_patentu_strzeleckiego = form.cleaned_data.get('nr_patentu_strzeleckiego')
			pre_licencja_sedziego = form.cleaned_data.get('licencja_sedziego')
			# form.cleaned_data['imie'] = 'assadasdsa@op.pl'
			context['registration_form'] = form

			context['pre_email'] = pre_email
			context['pre_username'] = pre_username
			context['pre_imie'] = pre_imie
			context['pre_nazwisko'] = pre_nazwisko
			# context['pre_data_urodzenia'] = pre_data_urodzenia.strftime("%Y.%m.%d")
			context['pre_data_urodzenia'] = pre_data_urodzenia.strftime("%d.%m.%Y")
			print(f'pre_data_urodzenia {context["pre_data_urodzenia"]}')
			# context['kod_poczowy'] = pre_kod_pocztowy
			context['pre_pesel'] = pre_pesel
			context['pre_nr_telefonu'] = pre_nr_telefonu
			context['pre_adres'] = pre_adres
			context['pre_kod_pocztowy'] = pre_kod_pocztowy
			context['pre_miejscowosc'] = pre_miejscowosc
			context['pre_imie_ojca'] = pre_imie_ojca
			context['pre_miejsce_urodzenia'] = pre_miejsce_urodzenia
			context['pre_licencja'] = pre_licencja
			context['pre_nr_patentu_strzeleckiego'] = pre_nr_patentu_strzeleckiego
			context['pre_licencja_sedziego'] = pre_licencja_sedziego
	else:
		# prre_mail = 'xxx@x.pl'
		# context['pre_mail'] = prre_mail
		form = BlogRegistrationForm()
		# context['pre_kod_pocztowy'] = 'asdsad'
		# context['pre_data_urodzenia'] = '01.05.2022'

		context['form'] = form
	return render(request, 'mainapp/blog_register.html', context)



class BlogUserView(ListView):
	# login_url = 'start'
	template_name = "mainapp/blog_user_view.html"
	model = Account
	context_object_name = 'Accounts'
	ordering = ['-date_joined']



# def view_accounts(request):
# 	accounts = Account.objects.all()
# 	data = [account.get_data() for account in accounts]
# 	response = {'data': data}
# 	return JsonResponse(response)

class BlogUserUpdateAdminView(LoginRequiredMixin, UpdateView):
	# login_url = 'start'
	template_name = "mainapp/blog_user_update.html"
	model = Account
	# form = BlogAccountAdminEdit
	form_class = BlogAccountAdminEdit
	# fields = ['imie', 'nazwisko', 'klub', 'data_urodzenia', 'adres', 'miejscowosc', 'licencja', 'pesel', 'nr_telefonu', 'kod_poczowy', 'miejscowosc', 'imie_ojca','miejsce_urodzenia', 'nr_patentu_strzeleckiego']

	# widgets = {'imie': TextInput(attrs={'class': "form-control",'style': 'max-width: 300px;','placeholder': 'Imię'}),
	# 'nazwisko': TextInput(attrs={'class': "form-control",'style': 'max-width: 300px;','placeholder': 'Nazwisko'}),
 #        }


	def get_success_url(self):
		return reverse("BlogUserView")
		
	# def form_valid(self, form):
	# 	return super(AccountUpdateView,self).form_valid(form)

	# def dispatch(self, request, *args, **kwargs):
	# 	try:
	# 		if request.user.rts:
	# 			return super(AccountUpdateView, self).dispatch(request, *args, **kwargs)
	# 		else:
	# 			return redirect('not_authorized')
	# 	except:
	# 		return redirect('not_authorized')

class Payment(View):
	# template_name = 'mainapp/payment_view.html'

	def get(self, request, *args, **kwargs):
		context = {}
		payments = LtsPayment.objects.filter(user=request.user)
		# print('--------------------------------------------------')

		for payment in payments:
			if payment.orderid is None:
				url = 'https://sandbox.przelewy24.pl/api/v1/transaction/by/sessionId/'+payment.sessionid
				r = requests.get(url, auth=HTTPBasicAuth('203257', '2c35b4a070f7a42d2a675c521e5331f8'))
				response_json = json.loads(r.text)
				try:
					payment.orderid=response_json['data']['orderId']
				except:
					payment.orderid=None
				payment.save()

		payments = LtsPayment.objects.filter(user=request.user)

		for payment in payments:
			if payment.result is None or payment.result!='success':
				# print(payment.result)
				n = hashlib.sha384()
				order_id2 = f'"sessionId":"{payment.sessionid}","orderId":{payment.orderid},"amount":5000,"currency":"PLN","crc":"0b45dd1983f5b90c"'
				order_id = '{'+order_id2+'}'
				# print(f'orderid: {order_id}')
				n.update(order_id.encode())
				sign_hash = n.hexdigest()
				# print(f'sign hasg: {sign_hash}')

				parameters = {"Content-Type":"application/json", "merchantId":203257, "posId":203257, "sessionId":payment.sessionid,  "amount": 5000, "currency": "PLN", "orderId": payment.orderid, "sign":sign_hash}
				r = requests.put('https://sandbox.przelewy24.pl/api/v1/transaction/verify', params=parameters, auth=HTTPBasicAuth('203257', '2c35b4a070f7a42d2a675c521e5331f8'))
				# print(r.status_code)
				# print(r.text)
				response_json = json.loads(r.text)
				try:
					payment.result=response_json['data']['status']
					payment.save()
				except:
					payment.result='Błąd'
					payment.save()

		context['payments'] = payments




		##############################
		# PAYMENT STATUS CHECK

		n = hashlib.sha384()
		order_id2 = '"sessionId":"admin@admin.com_2022_52624","orderId":317924410,"amount":5000,"currency":"PLN","crc":"0b45dd1983f5b90c"'
		# order_id2 = '"sessionId":"admin@admin.com_2022_26773","orderId":317938053,"amount":5000,"currency":"PLN","crc":"0b45dd1983f5b90c"'
		order_id = '{'+order_id2+'}'
		# print(f'orderid: {order_id}')
		n.update(order_id.encode())
		sign_hash = n.hexdigest()
		# print(f'sign hasg: {sign_hash}')

		parameters = {"Content-Type":"application/json", "merchantId":203257, "posId":203257, "sessionId":"admin@admin.com_2022_52624",  "amount": 5000, "currency": "PLN", "orderId": 317924410, "sign":sign_hash}
		r = requests.put('https://sandbox.przelewy24.pl/api/v1/transaction/verify', params=parameters, auth=HTTPBasicAuth('203257', '2c35b4a070f7a42d2a675c521e5331f8'))

		# print(r.status_code)
		# print(r.text)


		##############################


		return render(request, 'mainapp/payment_view.html', context)

	def post(self, request, *args, **kwargs):
		context = {}
		payments = LtsPayment.objects.filter(user=request.user)
		context['payments'] = payments
		# print(f'post request {request.body}')


		return render(request, 'mainapp/payment_view.html', context)


def payment_redirect(request):

	payment_user = request.user
	payment_year = 2022
	payment_amount = 5000
	payment_sessionid = request.user.email+'_'+str(payment_year)+'_'+str(random.randint(1,100000))
	# payment_sessionid = 'xxxxxx'

	
	# n = hashlib.sha384()
	# n.update(b'{"sessionId":"xxxxxx","merchantId":203257,"amount":5000,"currency":"PLN","crc":"0b45dd1983f5b90c"}')
	# sign_hash2 = n.hexdigest()
	# print(f'sign_hash2: {sign_hash2}')


	m = hashlib.sha384()
	update_string2 = f'"sessionId":"{payment_sessionid}","merchantId":203257,"amount":5000,"currency":"PLN","crc":"0b45dd1983f5b90c"'
	update_string = '{'+update_string2+'}'
	# print(f'update_string: {update_string}')
	m.update(update_string.encode())
	sign_hash = m.hexdigest()
	
	# print(f'sign_hash: {sign_hash}')
	

	parameters = {"Content-Type":"application/json", "sessionId":payment_sessionid, "merchantId":203257,"posId":203257,  "amount": payment_amount, "currency": "PLN", "description": "2022 ", "email": request.user.email, "country":"pl", "language":"pl", "urlReturn":"http://zawodyltstest.xyz/payment/", "urlStatus":"http://127.0.0.1:8000/post_payment/", "waitForResult":1, "sign":sign_hash}
	r = requests.post('https://sandbox.przelewy24.pl/api/v1/transaction/register', params=parameters, auth=HTTPBasicAuth('203257', '2c35b4a070f7a42d2a675c521e5331f8'))

	# print(r.status_code)
	# print(r.text)

	response_json = json.loads(r.text)



	# print(response_json['data']['token'])
	# print(sign_hash)
	# m = hashlib.sha384()
	# print('dupa')
	# response = HttpResponse()
	payment_instance = LtsPayment(user=request.user, amount=payment_amount, token=response_json['data']['token'], sessionid=payment_sessionid)
	payment_instance.save()



	n = hashlib.sha384()
	# order_id2 = f'"sessionId":"{payment_sessionid}", "orderId": "amount": {payment_amount}, "currency": "PLN", orderId":203257,"amount":5000,"currency":"PLN","crc":"0b45dd1983f5b90c"'
	order_id2 = '"sessionId":"admin@admin.com_2022_52624","orderId":317924410,"amount":5000,"currency":"PLN","crc":"0b45dd1983f5b90c"'
	order_id = '{'+order_id2+'}'
	# order_id = order_id2
	n.update(order_id.encode())
	sign_hash = n.hexdigest()

	######################################
	#	GET ORDER ID

	# parameters = {"Content-Type":"application/json", "sessionId":payment_sessionid, "merchantId":203257,"posId":203257,  "amount": payment_amount, "currency": "PLN", "description": "2022 ", "email": request.user.email, "country":"pl", "language":"pl", "urlReturn":"http://127.0.0.1:8000/payment/", "urlStatus":"http://127.0.0.1:8000/post_payment/", "waitForResult":1, "sign":sign_hash}
	# url_order_id_check = 'https://sandbox.przelewy24.pl/api/v1/transaction/by/sessionId/' + payment_sessionid
	# r = requests.get(url_order_id_check, auth=HTTPBasicAuth('203257', '2c35b4a070f7a42d2a675c521e5331f8'))
	# response_json = json.loads(r.text)
	# order_id = response_json['data']['orderId']

	# print(f'orderid: {order_id}')
	# print(f'response_json {response_json}')



	#####################################
	# parameters = {"Content-Type":"application/json", "merchantId":203257, "posId":203257, "sessionId":"admin@admin.com_2022_52624",  "amount": 5000, "currency": "PLN", "orderId": 317924410, "sign":sign_hash}
	# r = requests.put('https://sandbox.przelewy24.pl/api/v1/transaction/verify', params=parameters, auth=HTTPBasicAuth('203257', '2c35b4a070f7a42d2a675c521e5331f8'))


	return redirect('https://sandbox-go.przelewy24.pl/trnRequest/'+response_json['data']['token'])


def post_payment(request):
	# print('post payment')
	if request.method == 'POST':
		# print('post post payment')
		var = request.POST
		# print(var)

	# response = redirect('https://sandbox-go.przelewy24.pl/trnRequest/'+response_json['data']['token'])
	# print(f'response: {response}')
	# response = requests.get('https://sandbox-go.przelewy24.pl/trnRequest/'+response_json['data']['token'])
	# print(f'response text: {response.text}')
	# return 1
	# url = 'https://sandbox-go.przelewy24.pl/trnRequest/'+response_json['data']['token']
	# response = urlopen(url)

	# data_json = json.loads(response.read())
	# print(data_json)
	# return 1
	# redirect()

# class PaymentRedirect(View):

	# def get_context_data(self, **kwargs):
	# 	context = super().get_context_data(**kwargs)
	# 	context['token'] = self.kwargs['token']
	# 	return context



	# def get(self, request, *args, **kwargs):

		# m = hashlib.sha384()
		# m.update(b'{"sessionId":"203257","merchantId":203257,"amount":22,"currency":"PLN","crc":"0b45dd1983f5b90c"}')
		# r = requests.get('https://sandbox.przelewy24.pl/api/v1/testAccess', params=request.GET, auth=HTTPBasicAuth('203257', '2c35b4a070f7a42d2a675c521e5331f8'))


		# header = {"Content-Type":"application/json","X-Client-Id":"6786787678f7dd8we77e787","X-Client-Secret":"96777676767585",}
		# print(r.status_code)
		# print(r.text)
		# print(dir(r))
		# print(m.hexdigest())
		# print('dupa')


		# return render(request, 'mainapp/payment_view.html')



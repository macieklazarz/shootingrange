from django.db import models
from account.models import Account
from django.template.defaultfilters import slugify
from django.urls import reverse
from tinymce.models import HTMLField

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True, blank=True, verbose_name="Tytuł")
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    author = models.ForeignKey(Account, on_delete= models.CASCADE,related_name='blog_posts', verbose_name="Autor")
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField(verbose_name="Treść")
    created_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='featured_image/%Y/%m/%d/', blank=True, verbose_name="Zdjęcie")

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
    	if not self.slug:
    		self.slug = slugify(self.title)
    	return super().save(*args, **kwargs)

    def get_absolute_url(self):
    	return reverse('PostDetailView', kwargs={'slug':self.slug})

    def comments(self):
    	return PostComment.objects.filter(post=self)


class PostComment(models.Model):
	post = models.ForeignKey(Post, on_delete= models.CASCADE)
	author = models.ForeignKey(Account, on_delete= models.CASCADE, verbose_name="Autor")
	updated_on = models.DateTimeField(auto_now= True)
	content = models.TextField(verbose_name="Treść")
	created_on = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-created_on']

	def __str__(self):
		return 'Komentarz dodany przez {}'.format(self.author)



class ForumTopic(models.Model):
    topic = models.CharField(max_length=200, unique=True, blank=True, verbose_name='Temat')
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    author = models.ForeignKey(Account, on_delete= models.CASCADE, verbose_name="Autor")

    def __str__(self):
        return self.topic


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.topic)
        return super().save(*args, **kwargs)

    def get_posts(self):
        return ForumPost.objects.filter(topic=self)

class ForumPost(models.Model):
    topic = models.ForeignKey(ForumTopic, on_delete= models.CASCADE, verbose_name='Temat')
    title = models.CharField(max_length=200, unique=True, blank=True, verbose_name='Tytuł')
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    author = models.ForeignKey(Account, on_delete= models.CASCADE)
    content = HTMLField(verbose_name='Treść')
    created_on = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-created_on']


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def last_comment(self):
        return ForumComment.objects.filter(post=self).order_by('-created_on')


    def post_comments(self):
        return ForumComment.objects.filter(post=self).order_by('-created_on')



class ForumComment(models.Model):
    post = models.ForeignKey(ForumPost, on_delete= models.CASCADE, verbose_name='post')
    author = models.ForeignKey(Account, on_delete= models.CASCADE)
    content = HTMLField(verbose_name='Treść')
    created_on = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-created_on']


    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.title)
    #     return super().save(*args, **kwargs)


class LtsPayment(models.Model):
    user = models.ForeignKey(Account, on_delete= models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    year = models.IntegerField(default=2022)
    amount = models.IntegerField(default=0)
    result = models.CharField(null=True, max_length=200)
    token = models.CharField(max_length=200)
    sessionid = models.CharField(max_length=200)
    orderid = models.IntegerField(null=True)

    class Meta:
        ordering = ['-created_on']
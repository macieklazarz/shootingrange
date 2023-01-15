from django.contrib import admin


from .models import Post, PostComment, ForumTopic, ForumPost, ForumComment, LtsPayment

# admin.site.register(Post)

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'created_on')
	search_fields = ('title', 'author')

@admin.register(PostComment)
class PostCommentAdmin(admin.ModelAdmin):
	list_display = ('author', 'created_on', 'post')
	search_fields = ('author',)


@admin.register(ForumTopic)
class ForumTopicAdmin(admin.ModelAdmin):
	list_display = ('author', 'topic')
	search_fields = ('author', 'topic')

@admin.register(ForumPost)
class ForumPostAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'created_on')
	search_fields = ('title', 'author', 'created_on')


@admin.register(ForumComment)
class ForumCommentAdmin(admin.ModelAdmin):
	list_display = ('author', 'created_on')
	search_fields = ('author', 'created_on')

@admin.register(LtsPayment)
class LtsPaymentAdmin(admin.ModelAdmin):
	list_display = ('user', 'year', 'created_on', 'result')
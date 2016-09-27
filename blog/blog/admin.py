from django.contrib import admin
from blog.models import Article, Category

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'create_time', 'category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
# admin.site.register(UserProfile)

from django.contrib import admin

# Register your models here.

from . models import Category, Product

# admin.site.register(Category)

# admin.site.register(Product)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('name',)}

    search_fields = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('title',)}

    list_display = ['artist', 'title', 'category']

    list_filter = ['category']

    search_fields = ['artist', 'title']

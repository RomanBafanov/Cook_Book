from django.contrib import admin
from .models import *


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'number_of_uses')
    list_display_links = ('id', 'product_name')
    search_fields = ('id', 'product_name')


class DishAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_of_the_dish')
    list_display_links = ('id', 'name_of_the_dish')
    search_fields = ('id', 'name_of_the_dish')


class RecipeProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'recipe', 'product', 'weight')
    list_display_links = ('id', 'recipe', 'product')
    search_fields = ('recipe', 'product')
    list_editable = ('weight',)
    list_filter = ('recipe', 'product')


admin.site.register(Products, ProductsAdmin)
admin.site.register(Dish, DishAdmin)
admin.site.register(RecipeProduct, RecipeProductAdmin)

from django.db import models


class Products(models.Model):
    product_name = models.CharField(verbose_name='Название продукта', max_length=64)
    number_of_uses = models.IntegerField(verbose_name='Количество приготовлений', default=0)

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = 'Продукты'
        verbose_name_plural = 'Продукты'
        ordering = ['product_name']


class Dish(models.Model):
    name_of_the_dish = models.CharField(verbose_name='Название блюда', max_length=64)

    def __str__(self):
        return self.name_of_the_dish

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюдо'
        ordering = ['name_of_the_dish', ]


class RecipeProduct(models.Model):
    recipe = models.ForeignKey(Dish, on_delete=models.CASCADE, verbose_name='Название блюда')
    product = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name='Название продукта')
    weight = models.IntegerField(verbose_name='Вес продукта в граммах')

    class Meta:
        unique_together = ('recipe', 'product',)
        verbose_name = 'Продукты для блюд'
        verbose_name_plural = 'Продукты для блюд'
        ordering = ['recipe', ]

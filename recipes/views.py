from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def add_product_to_recipe(request):
    if request.GET:
        recipe_id = request.GET.get('recipe_id')
        product_id = request.GET.get('product_id')
        weight = int(request.GET.get('weight'))
        product = Products.objects.get(pk=product_id)
        dish = Dish.objects.get(pk=recipe_id)
        name = dish.name_of_the_dish
        if RecipeProduct.objects.filter(recipe=recipe_id, product=product_id):
            recipe = RecipeProduct.objects.get(recipe=recipe_id, product=product_id)
            if recipe.weight != weight:
                recipe.weight = weight
                recipe.save()
                return HttpResponse(content=f"<h3>В рецепте {name} продукт {product} изменён на вес {weight}</h3>")
            else:
                return HttpResponse(content="<h3>Такой продукт с таким же весом уже есть в этом рецепте</h3>")
        else:
            RecipeProduct.objects.create(recipe=dish, product=product, weight=weight)
            return HttpResponse(content=f"<h3>{product} добавлен в рецепт {name}</h3>")
    else:
        return HttpResponse(content="<h3>Функция добавляет к указанному рецепту указанный "
                                    "продукт с указанным весом. Если в рецепте уже есть "
                                    "такой продукт, то функция должна поменять его вес в "
                                    "этом рецепте на указанный. Необходимые параметры - "
                                    "recipe_id, product_id, weight</h3>")


def cook_recipe(request):
    if request.GET:
        recipe_id = request.GET.get('recipe_id')
        products = RecipeProduct.objects.filter(recipe=recipe_id)
        for name in products:
            product = Products.objects.get(product_name=name.product)
            product.number_of_uses += 1
            product.save()

        return HttpResponse(content=f"<h3>Блюдо приготовлено!</h3>")
    else:
        return HttpResponse(content="<h3>Функция увеличивает на единицу количество приготовленных "
                                    "блюд для каждого продукта, входящего в указанный рецепт. "
                                    "Необходимый параметр - recipe_id</h3>")


def show_recipes_without_product(request):
    if request.GET:
        product_id = request.GET.get('product_id')
        more_gram = RecipeProduct.objects.filter(product=product_id, weight__gt=10)
        less_gram = RecipeProduct.objects.filter(product=product_id, weight__lt=10)

        return render(request, 'recipes/show.html', {'more_gram': more_gram, 'less_gram': less_gram})
    else:
        return HttpResponse(content="<h3>Функция возвращает HTML страницу, на которой размещена таблица. "
                                    "В таблице отображены id и названия всех рецептов, в которых указанный "
                                    "продукт отсутствует, или присутствует в количестве меньше 10 грамм. "
                                    "Необходимый параметр - recipe_id</h3>")

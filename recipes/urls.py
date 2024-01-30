from django.urls import path
from .views import *

urlpatterns = [
    path('api/v1/add', add_product_to_recipe),
    path('api/v1/cook', cook_recipe),
    path('api/v1/show', show_recipes_without_product),
]
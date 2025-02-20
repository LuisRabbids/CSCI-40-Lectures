from django.urls import path
from .views import recipes_lists, first_recipe, second_recipe

urlpatterns = [
    path('recipes/list', recipes_lists, name="recipes-lists"), 
    path('recipe/1', first_recipe, name="first-recipe"),
    path('recipe/2', second_recipe, name="second-recipe"),
]

app_name = 'ledger'
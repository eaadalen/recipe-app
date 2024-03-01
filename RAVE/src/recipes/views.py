from django.shortcuts import render
from django.views.generic import ListView, DetailView   #to display lists
from .models import Recipe                #to access Recipe model
#to protect class-based view
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def home(request):
   return render(request, '../templates/recipes/recipes_home.html')

# Create your views here.
class RecipeListView(LoginRequiredMixin, ListView):           #class-based view
   model = Recipe                         #specify model
   template_name = '../templates/recipes/recipe_list.html'    #specify template 

class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = "../templates/recipes/recipe_details.html"
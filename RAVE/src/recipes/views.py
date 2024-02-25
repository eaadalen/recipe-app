from django.shortcuts import render

# Create your views here.
def home(request):
   return render(request, '../templates/recipes/recipes_home.html')
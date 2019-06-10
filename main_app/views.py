from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
class Dog:
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age

dogs = [
    Dog('Saide', 'Golden', 'Good Dog', 3),
    Dog('Max', 'Boxer', 'Shy Guy', 0),
    Dog('Mindy', 'Bull Dog', 'Mean Jerk', 4)
]


def home(request):
    return HttpResponse('<hl> Woof <h1>')

def about(request):
    return render(request, 'about.html')

def dogs_index(request):
    return render(request, 'dogs/index.html', { 'dogs': dogs })
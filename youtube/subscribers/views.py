from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Friend

# Create your views here.


class DisplayFriends(ListView):
    model = Friend
from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Ad
from .owner import *


# Create your views here.


class AdListView(OwnerListView):
    model = Ad
    context_object_name = 'ad_list'


class AdDetailView(OwnerDetailView):
    model = Ad


class AdCreateView(OwnerCreateView):
    model = Ad
    fields = ['title', 'price', 'text']
    success_url = reverse_lazy('ads:all')


class AdUpdateView(OwnerUpdateView):
    model = Ad
    fields = ['title', 'price', 'text']
    success_url = reverse_lazy('ads:all')


class AdDeleteView(OwnerDeleteView):
    model = Ad
    fields = ['title', 'price', 'text']
    success_url = reverse_lazy('ads:all')

from django.shortcuts import render
import random

# Create your views here.

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import generic, View
from django.utils import timezone

from .models import AmazonLabels, AmazonProductReviews

class Clone_indexView(generic.TemplateView):
    template_name = "final_lab/clone_index.html"

class IndexView(generic.TemplateView):
    template_name = "final_lab/index.html"

class BaseView(generic.TemplateView):
    template_name = "final_lab/base.html"

# def cat_view(request):
#     return render(request, 'final_lab/cat.html')

# def index_view(request, category):
#     label = ?
#     return render(request, 'final_lab/category.html', {'category': category, 'label': label})

def index_view(request, category):
    try:
        label = AmazonLabels.objects.get(cat_name=category)
    except AmazonLabels.DoesNotExist:
        label = None
        rnd_txt = None
    else:
        reviews_with_label = AmazonProductReviews.objects.filter(label=label)
        if reviews_with_label.exists():
            rnd_txt = random.choice(reviews_with_label).reviewText
        else:
            rnd_txt = None

    return render(request, 'final_lab/category.html', {'category': category, 'label_cat': label, 'reviewText': rnd_txt})

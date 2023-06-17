from django.shortcuts import render

# Create your views here.

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import AmazonLabels, AmazonProductReviews

class Clone_indexView(generic.TemplateView):
    template_name = "final_lab/clone_index.html"

class IndexView(generic.TemplateView):
    template_name = "final_lab/index.html"

class BaseView(generic.TemplateView):
    template_name = "final_lab/base.html"

from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from rest_framework import viewsets
from django.http import JsonResponse

import tensorflow as tf
import numpy, subprocess, wikipediaapi, sys

# Create your views here.
@csrf_exempt
def hello(request):
    return JsonResponse({'msg':'Hello World'})

@csrf_exempt
def register(request):
    if request.method == 'POST':
        if request.POST['username'] and request.POST['password']:
            pass


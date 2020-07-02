from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse,JsonResponse
from . import dictapi

from .models import Word
from time import localtime
from datetime import datetime

def Query(request):
    account = request.
    return JsonResponse(data={})
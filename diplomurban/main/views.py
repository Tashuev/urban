from django.shortcuts import render
from django.http import HttpResponse

def index1(request):
    return HttpResponse("<h4>ПРОВЕРКА</h4>")


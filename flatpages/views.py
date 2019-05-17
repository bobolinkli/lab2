#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse(u'Привет, мир!'.encode('cp1251'), mimetype="text/plain")
    return render(request, 'static_handler.html', {})

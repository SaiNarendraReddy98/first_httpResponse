from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def Demo(request):
    return HttpResponse('<h1 style="color:green;background-color:cyan;"><marquee>Hai iam Demo how are you</h1></marquee>')

def Nani(request):
    return HttpResponse('<h1 style="padding:50px;color:orange;"><marquee>Hai iam Narendra Reddy welcome</marquee></h1>')

def hello(request):
    return HttpResponse('<h1 style="padding:150px;color:Green"><marquee>Hai Iam From Visakhapatnam Welcome To Green City...</marquee></h1>') 





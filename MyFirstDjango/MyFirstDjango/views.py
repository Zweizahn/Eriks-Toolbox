from django.http import HttpResponse

def hello_world(response):
    return HttpResponse('Hello Erik!')
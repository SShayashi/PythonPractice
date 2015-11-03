from datetime import datetime
from django.http.response import HttpResponse
from django.shortcuts import render


def hello_world(request):
    return HttpResponse('Hello World')

def hello_template(request):
    d = {
        'hour': datetime.now().hour,
        'message': 'Sample message',
    }
    return render(request,'index.html' , d)

def hello_if(request):
    d = {
        'is_visible':False,
        'empty_str': '',
    }
    return render(request, 'if.html', d)

def hello_for(request):
    d = {
        'objects':range(10),
    }
    return render(request , 'for.html',d)

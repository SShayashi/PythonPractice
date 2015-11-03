from datetime import datetime
from django.http.response import HttpResponse
from django.shortcuts import render


def hello_world(requet):
    return HttpResponse('Hello World')

def hello_template(requet):
    d = {
        'hour': datetime.now().hour,
        'message': 'Sample message',
    }
    return render(requet,'index.html' , d)

def hello_if(requet):
    d = {
        'is_visible':False,
        'empty_str': '',
    }
    return render(requet, 'if.html', d)

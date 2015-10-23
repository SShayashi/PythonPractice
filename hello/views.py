from django.http.response import HttpResponse

def hello_world(requet):
    return HttpResponse('Hello World')

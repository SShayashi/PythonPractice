from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Message
from .forms import MessageForm


def index(request):
    return render(request,'crud/index.html', {})

def add(request):
    return render(request, 'crud/edit.html', {})


def edit(request, editing_id):
    return render(request, 'crud/edit.html', {})


def delete(request):
    return HttpResponse('Delete')

def index(request):
    d = {
        'messages': Message.objects.all(),
    }
    return render(request, 'crud/index.html', d)

def add(request):
    form = MessageForm(request.POST or None)
    if form.is_valid():
        Message.objects.create(**form.cleaned_data)
        return redirect('crud:index')

    d = {
        'form': form,
    }
    return render(request, 'crud/edit.html', d)

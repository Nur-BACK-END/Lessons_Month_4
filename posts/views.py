from django.shortcuts import render
from django.http import HttpResponse

def text_response(request):
    return HttpResponse("Это текстовый ответ от Django!")

def html_response(request):
    return render(request, 'main.html', {'title': 'HTML Страница'})



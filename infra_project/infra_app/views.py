from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('У меня получилось!')
   # text = 'У меня получилось!'
   # return render(request, 'first_page.html', {'text': text})

def second_page(request):
    return HttpResponse('А это вторая страница!')
   # text = 'А это вторая страница'
   # return render(request, 'second_page.html', {'text': text})

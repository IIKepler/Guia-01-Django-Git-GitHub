from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("""<h1 style=color:red> Guía N1</h1>
                        <p style=color:blue>Soy un texto azul</p>""")

def text(request):
    return HttpResponse("""<h2>Muchas A</h2>
                        <p>aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa""")
def img(request):
    return HttpResponse("<img src='https://cdn.prod.website-files.com/5f5a53e153805db840dae2db/64e79ca5aff2fb7295bfddf9_github-que-es.jpg' alt='GitHub'>")
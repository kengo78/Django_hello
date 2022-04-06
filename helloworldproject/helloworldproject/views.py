from http.client import HTTPResponse


from django.http import HttpResponse
from django.views.generic import TemplateView
from pathlib import Path

def helloworldfunction(request):
    returnedobject = HttpResponse('<h1>helloworld</h1>')
    return returnedobject

def someview(request):
    print(Path(__file__).resolve())
    return HttpResponse('')
    

class HelloWorldClass(TemplateView):
    #どのhtmlファイルを持ってきますか ファイルの場所を書く、
    template_name = 'hello.html'
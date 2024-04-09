from django.shortcuts import render
from django.shortcuts import get_list_or_404
from django.http import HttpResponse
from django.template import loader

from core.models import Produto

def index (request):
    produtos = Produto.objects.all()
    prod = {
        'curso': 'Programação em Python Django Framework',
        'outro': 'Aprendendo Django',
        'produtos': produtos
    }

    return render(request, 'index.html', prod)

def contact (request):
    return render(request, 'contact.html')

def produto (request, pk):
    #produto = Produto.objects.get(id=pk)
    produto = get_list_or_404(Produto, id=pk)
    context = {
        'produto': produto
    }
    return render (request, 'produto.html', context)

def error404 (request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text-html; charset: utf8', status= 404)

def error500 (request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text-html; charset: utf8', status= 500)
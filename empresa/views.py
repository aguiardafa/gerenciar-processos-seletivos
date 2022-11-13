from django.shortcuts import render
from django.http import HttpResponse


def nova_empresa(request):
    return HttpResponse('Página de nova_empresa')

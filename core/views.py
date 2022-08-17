from django.shortcuts import render, HttpResponse


# Create your views here.

def hello(request, num1, num2):
    texto = "<h1>Primeiro numero: {} segundo: {} </h1>".format(num1, num2)

    soma = num1 + num2

    multiplicacao = num1 * num2

    contas = "<h2>soma: {} </h2>" \
             "<h2>multiplicacao: {}".format(soma, multiplicacao)

    tela = (texto + " " + contas)

    return HttpResponse({tela})

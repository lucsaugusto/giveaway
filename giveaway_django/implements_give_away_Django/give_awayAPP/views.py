from django.shortcuts import render

def index(resquest):
    return render(resquest, 'index.html')

def cadastro(resquest):
    return render(resquest, 'cadastro.html')

def doacao(resquest):
    return render(resquest, 'doacao.html')

def item(resquest):
    return render(resquest, 'item.html')

def login(resquest):
    return render(resquest, 'login.html')

def products(resquest):
    return render(resquest, 'products.html')







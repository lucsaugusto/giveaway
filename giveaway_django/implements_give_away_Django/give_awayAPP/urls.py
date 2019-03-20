from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('doacao/', views.doacao, name='doacao'),
    path('item/', views.item, name='item'),
    path('login/', views.login, name='login'),
    path('produtos/', views.products, name='products'),
]

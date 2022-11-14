from django.urls import path
from . import views

urlpatterns = [
    path('empresas/', views.empresas, name="empresa"),
    path('nova_empresa/', views.nova_empresa, name="nova_empresa")

]

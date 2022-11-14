from django.urls import path
from . import views

urlpatterns = [
    path('empresas/', views.empresas, name="empresa"),
    path('nova_empresa/', views.nova_empresa, name="nova_empresa"),
    path('excluir_empresa/<int:id>', views.excluir_empresa, name="excluir_empresa"),

]

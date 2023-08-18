from django.urls import path
from . import views

# Mapea las URLs a funciones callback de Python («vistas»)
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('saludar/<str:nombre>', views.saludar, name='saludar'),
    path('moneda/', views.moneda, name='moneda'),
    path('contacto/', views.contacto, name='contacto'),
    path('nosotros/', views.nosotros, name='nosotros'),
]

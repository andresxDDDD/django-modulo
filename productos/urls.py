from django.urls import path
from . import views
# 2 punto de entrada y aca se manejan todas las rutas (url) de esta aplicacion 
urlpatterns = [
    path('', views.index, name='home_productos'),
]
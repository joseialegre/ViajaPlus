from django.urls import path
from .views import my_view  # Asegúrate de importar tu vista correctamente

urlpatterns = [
    path('', my_view, name='home'),
]
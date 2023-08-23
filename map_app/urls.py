from django.urls import path
from .views import map_view

app_name = 'map_app'  # Добавьте это, чтобы уточнить пространство имен приложения

urlpatterns = [
    path('', map_view, name='map_view'),  # Пример URL-пути для отображения карты
]

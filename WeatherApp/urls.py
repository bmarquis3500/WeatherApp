from django.urls import path
from django.views.generic import TemplateView

from WeatherApp.views import MyLocationWeather


urlpatterns = [
    
    path('', MyLocationWeather.as_view(template_name='MyWeather.html'))
]
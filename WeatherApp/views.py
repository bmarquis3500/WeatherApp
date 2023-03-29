from django.shortcuts import render
from django.views.generic import TemplateView
from openmeteo_py import Hourly,Daily,Options,OWmanager

# Create your views here.


class MyLocationWeather(TemplateView):
    
    

    def get(self, request):

        latitude = 39.1955
        longitude = 76.7228

        hourly = Hourly()
        daily = Daily()
        options = Options(latitude, longitude)

        mgr = OWmanager(options,
                    hourly.temperature_2m())
        meteo = mgr.get_data()
        temp = meteo['hourly']['temperature_2m'][0]

        tempF=(temp*(9/5))+32




        #temp = str(Hourly.temperature_2m)
        #print(temp)
        context = {'temp' : tempF}
        return render(request,'MyWeather.html', context)
    
    #print(meteo)

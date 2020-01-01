from django.shortcuts import render
import requests

def index(request):

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=fd5060bdf66d198bf9a19861e3e4a92c'
    city = 'Las Vegas'
    city_weather = requests.get(url.format(city)).json()

    weather = {
        'city': city,
        'temperature': city_weather['main']['temp'],
        'description': city_weather['weather'][0]['description'],
        'icon': city_weather['weather'][0]['icon']
    }

    context = {'weather': weather}

    return render(request, 'weather/index.html', context)

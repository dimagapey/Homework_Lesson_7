import requests
import datetime


URL = 'http://api.openweathermap.org/data/2.5/forecast/daily'


def return_weather(days=1):
    data = {'q': 'Odesa', 'units': 'metric', 'cnt': days,
            'appid': 'f9ada9efec6a3934dad5f30068fdcbb8'}
    r = requests.get(URL, data)
    return r.json()


result = return_weather(days=5)
with open('dayweather.txt', 'w') as f:
    f.writelines(['  Date   ', '     Day   ', '    Night  ', '\n '])
    for day in result['list']:
        f.writelines([datetime.date.fromtimestamp(day['dt']).strftime('%d-%m-%Y') + (5 * ' '),
                     str(day['temp']['day']) + (5 * ' '),
                     str(day['temp']['night']) + (5 * ' '), '\n'])
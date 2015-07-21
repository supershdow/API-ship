import urllib2
import json

def get_weather(city='nyc'):
    url="http://api.openweathermap.org/data/2.5/weather?q="+city
    u=urllib2.urlopen(url)
    result=u.read()
    w=json.loads(result)
    return w['main']['temp']

def toFahrenheit(K):
    C=K-273.15
    F=(C*9/5)+32
    return F

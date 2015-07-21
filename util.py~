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

def flickr(query="Sloth"):
    url="https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=c7914973b11b169e5bc76685e4dfa805&tags=%s&format=json&nojsoncallback=1"%query
    u=urllib2.urlopen(url)
    result=u.read()
    w=json.loads(result)
    return w['photos']['photo']

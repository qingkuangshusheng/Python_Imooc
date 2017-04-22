#coding:utf-8
from collections import Iterable,Iterator
import requests
class WeatherIterator(Iterator):
    def __init__(self,cities):
        self.cities=cities
        self.index=0
    def getWeather(self,city):
        r=requests.get(u'http://wthrcdn.etouch.cn/weather_mini?city='+city)
        #html=urllib2.urlopen(u'http://wthrcdn.etouch.cn/weather_mini?city='+city)
        data=r.json()['data']['forecast'][0]
        return '%s:%s,%s'%(city,data['low'],data['high'])
    def next(self):
        if self.index==len(self.cities):
            raise StopIteration
        city=self.cities[self.index]
        self.index+=1
        return self.getWeather(city)
class WeatherIterable(Iterable):
    def __init__(self,cities):
        self.cities=cities
    def __iter__(self):
        return WeatherIterator(self.cities)
#化简版
# class WeatherIterable(Iterable):
#     def __init__(self,cities):
#         self.cities=cities
#         self.index=0
#     def __iter__(self):
#         return self
#     def getWeather(self,city):
#         r=requests.get(u'http://wthrcdn.etouch.cn/weather_mini?city='+city)
#         #html=urllib2.urlopen(u'http://wthrcdn.etouch.cn/weather_mini?city='+city)
#         data=r.json()['data']['forecast'][0]
#         return '%s:%s,%s'%(city,data['low'],data['high'])
#     def next(self):
#         if self.index==len(self.cities):
#             raise StopIteration
#         city=self.cities[self.index]
#         self.index+=1
#         return self.getWeather(city)

if __name__ == '__main__':
    for i in WeatherIterable([u'郑州',u'北京',u'上海',u'广州',u'深圳',u'杭州']):
        print i


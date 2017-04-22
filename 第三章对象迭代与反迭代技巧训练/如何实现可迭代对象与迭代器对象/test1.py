#coding:utf-8
import requests
def getWeather(city):
    r=requests.get(u'http://wthrcdn.etouch.cn/weather_mini?city='+city)
    #html=urllib2.urlopen(u'http://wthrcdn.etouch.cn/weather_mini?city='+city)
    data=r.json()['data']['forecast'][0]
    return '%s:%s,%s'%(city,data['low'],data['high'])
print getWeather(u'北京')
print getWeather(u'郑州')


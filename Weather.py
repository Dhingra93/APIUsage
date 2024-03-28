import requests
import pandas as pd
import os
from datetime import datetime

"""
SITE : https://openweathermap.org/

API URL :=f'https://api.openweathermap.org/data/2.5/forecast?q={loc}&appid={apikey}&units=metric'
"""

def getWeather(loc,apikey="c5b24a8d8c3803eafdce1e5fea4fa5a3"):
    url=f'https://api.openweathermap.org/data/2.5/forecast?q={loc}&appid={apikey}&units=metric'
    r=requests.get(url)
    content=r.json()
    timeofweather=[]
    temp_min=[]
    temp_max=[]
    windspeed=[]
    for dicto in content['list']:
        timeofweather.append(dicto['dt_txt'])
        temp_min.append(dicto['main']['temp_min'])
        temp_max.append(dicto['main']['temp_max'])
        windspeed.append(dicto['wind']['speed'])
    dict = {'Time of Weather': timeofweather,
            'Min Temp' : temp_min,
            'Max Temp': temp_max,
            'Windspeed' : windspeed}
    df = pd.DataFrame(dict)
    return df

def createfile(city,df):
    filename = city + "_" + datetime.now().strftime("%d-%m-%Y") + ".csv"
    if os.path.exists(filename):
        os.remove(filename)
    df.to_csv(filename)

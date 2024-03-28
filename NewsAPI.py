import requests
import pandas as pd
import os
from datetime import datetime

"""
API URL : 
url = f'https://newsapi.org/v2/everything?qInTitle={topic}&from={fromDate}&to={toDate}8&sortBy=popularity&language={langauge}&apiKey={apikey}'
    
URL : "SpaceNEWS"    

"""


def getNews(topic,fromDate,toDate,langauge="en",apikey="de588a432f084350a3f8a89a992641b2"):
    url = f'https://newsapi.org/v2/everything?qInTitle={topic}&from={fromDate}&to={toDate}8&sortBy=popularity&language={langauge}&apiKey={apikey}'
    r=requests.get(url)
    content=r.json()
    articles=content["articles"]
    title = []
    description=[]

    for article in articles:
        title.append(article['title'])
        description.append(article['description'])
    return title,description

def CreateCSVFromList(subject,lst1,lst2):
    # dictionary of lists
    dict = {'Column1': lst1, 'Column2':lst2}
    df = pd.DataFrame(dict)
    # saving the dataframe
    filename=subject+"_"+datetime.now().strftime("%d-%m-%Y")+".csv"
    if os.path.exists(filename):
        os.remove(filename)
    df.to_csv(filename)

def getNewsForCountry(country,apikey="de588a432f084350a3f8a89a992641b2"):
    url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={apikey}'
    r=requests.get(url)
    content=r.json()
    articles=content["articles"]
    title = []
    description=[]

    for article in articles:
        title.append(article['title'])
        description.append(article['description'])
    return title,description


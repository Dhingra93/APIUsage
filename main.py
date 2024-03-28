from NewsAPI import *
from Weather import *
from CreateApi import *
from Facebook import *
from TryPostAPI import *



"""
lst1,lst2=getNews(topic="Movies",fromDate="2024-03-01",toDate="2024-03-26")
CreateCSVFromList(subject='Movies',lst1= lst1,lst2=lst2)

lst1,lst2=getNewsForCountry(country="US")
CreateCSVFromList(subject="US",lst1=lst1,lst2=lst2)
"""


""""
df=getWeather(loc="New Delhi")
createfile("New Delhi",df)
"""

#createFun()

#test()

print(trypost(word="Helo",lang="en-US"))
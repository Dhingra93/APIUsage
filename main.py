from NewsAPI import getNews,CreateCSVFromList

lst1,lst2=getNews(topic="Movies",fromDate="2024-03-01",toDate="2024-03-26")
CreateCSVFromList(lst1,lst2)
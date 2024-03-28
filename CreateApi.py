from flask import Flask,jsonify
from bs4 import BeautifulSoup
import requests


def currency(inCurrency,outCurrency):
    url=f"https://www.x-rates.com/calculator/?from={inCurrency}&to={outCurrency}&amount=1"
    content=requests.get(url).text
    soup=BeautifulSoup(content,"html.parser")
    cur=soup.find("span",class_="ccOutputRslt").get_text()
    return cur.replace(outCurrency,"").strip()

def createFun():
    app=Flask(__name__)

    @app.route('/')
    def home():
        return '<h1>Currency Rate API</h1> <p>Example URL: /api/v1/usd-eur</p>'

    @app.route('/api/v1/<in_cur>-<out_cur>')
    def rateConverter(in_cur,out_cur):
        rate=currency(in_cur,out_cur)
        dicto={"Input Currency": in_cur, "Output Currency" : out_cur,"Rate":rate}
        return jsonify(dicto)



    app.run(host="0.0.0.0")
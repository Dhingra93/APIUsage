import json

import requests

def trypost(word,lang):
    url="https://api.languagetool.org/v2/check"
    data={
        'text':word,
        'language':lang
          }
    response=requests.post(url,data=data)
    result=json.loads(response.text)
    possibly=[]
    for res in result['matches']:
        for val in res['replacements']:
            possibly.append(val['value'])
    return  possibly
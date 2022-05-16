import requests
import json

url = 'http://180.83.19.43:7579/Mobius'
header = {'Accept':'application/json',
'X-M2M-RI' :'12345',
'X-M2M-Origin':'S',
'Content-Type':'application/vnd.onem2m-res+json;ty=2'
}

datas = {"m2m:ae" : {
    "rn": "test2",
    "api": "0.2.481.2.0001.001.000111",
    "lbl": ["key1", "key2"],
    "rr": 'true',
    "poa": ["http://203.254.173.104:9727"]
    }
}

resp = requests.post(url=url, headers=header, data = json.dumps(datas))
print(resp.status_code)
print(resp.text)

from signature import get_sign
import requests
import json

ApiKey = 'mx0vglo09a68ctj7tf'
ApiSec = '0d7038e59c2a431784e9c9ee534751ec'
req_method = 'post'

url = "https://contract.mexc.com/api/v1/private/position/change_margin"

params = {
    "positionId":279313529050999808,
    "amount":1,
    "type":"ADD"
}

sign = get_sign(api_key=ApiKey, api_sec=ApiSec, params=params, req_method=req_method)

headers = {
    "Request-Time": sign["stemp"],
    "ApiKey": ApiKey,
    "Content-Type": "application/json",
    "Signature": sign["code"],
}

p = requests.post(url, headers=headers, data=params)

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(p.json(), f, ensure_ascii=False, indent=4)

print(p.text)

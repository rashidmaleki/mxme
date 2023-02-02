from signature import get_sign
import requests
import json

ApiKey = 'mx0vglo09a68ctj7tf'
ApiSec = '0d7038e59c2a431784e9c9ee534751ec'
req_method = 'get'
sign = get_sign(api_key=ApiKey, api_sec=ApiSec, req_method=req_method)

url = 'https://contract.mexc.com/api/v1/private/account/assets'

headers = {
    "Request-Time": sign['stemp'],
    "ApiKey": ApiKey,
    "Content-Type": "application/json",
    'Signature': sign['code'],
}

p = requests.get(url, headers=headers)

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(p.json(), f, ensure_ascii=False, indent=4)

print(p)

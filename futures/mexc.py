import hashlib
import hmac
import time
import requests
import json
from json import dumps

def get_sign(api_key, api_sec, req_method, params=None):
    ApiKey = api_key
    ApiSec = api_sec
    stemp = str(int(time.time() * 1000))

    if req_method == "post":
        objectString = ApiKey + stemp + params

        h = hmac.new(bytes(ApiSec, 'utf-8'),
                     bytes(objectString, 'utf-8'), hashlib.sha256)
        sign = {
            'stemp': stemp,
            'code': h.hexdigest()
        }
        return sign

    elif req_method == "get":
        objectString = ApiKey + stemp

        h = hmac.new(bytes(ApiSec, 'utf-8'),
                     bytes(objectString, 'utf-8'), hashlib.sha256)

        sign = {
            'stemp': stemp,
            'code': h.hexdigest()
        }
        return sign


class MexcApi:
    def __init__(self, api_key, api_sec, params):
        self.api_key = api_key
        self.api_sec = api_sec
        self.params = params

    def order_cancel_all(self):
        url = "https://contract.mexc.com/api/v1/private/order/cancel_all"

        sign = get_sign(api_key=self.api_key, api_sec=self.api_sec,
                        params=self.params, req_method="post")

        headers = {
            "Request-Time": sign["stemp"],
            "ApiKey": self.api_key,
            "Content-Type": "application/json",
            "Signature": sign["code"],
        }

        p = requests.post(url, headers=headers, data=self.params)

        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(p.json(), f, ensure_ascii=False, indent=4)

        return p.json()


    def account_assets(self):
        sign = get_sign(api_key=self.api_key,
                        api_sec=self.api_sec, req_method="get")

        url = 'https://contract.mexc.com/api/v1/private/account/assets'

        headers = {
            "Request-Time": sign['stemp'],
            "ApiKey": self.api_key,
            "Content-Type": "application/json",
            'Signature': sign['code'],
        }

        p = requests.get(url, headers=headers)

        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(p.json(), f, ensure_ascii=False, indent=4)
        return p.json()

    def order_new(self):
        url = "https://contract.mexc.com/api/v1/private/order/submit"

        sign = get_sign(api_key=self.api_key, api_sec=self.api_sec,
                        params=self.params, req_method="post")

        headers = {
            "Request-Time": sign["stemp"],
            "ApiKey": self.api_key,
            "Content-Type": "application/json",
            "Signature": sign["code"],
        }

        p = requests.post(url, headers=headers, data=self.params)

        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(p.json(), f, ensure_ascii=False, indent=4)

        return p.json()

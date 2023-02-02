import hashlib
import hmac
import base64
import time

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

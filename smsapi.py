#!/usr/bin/env python
#-*-coding:utf-8-*-

import requests

#SMS_TO = tos
#SMS_CONTENT = content
TELAPI_TOKEN = "你的token"
TELAPI_SMS_URL = "你的sms URL"

def sendsms(phones,content,type=None):
    try:
        data = {
            "type" : TELAPI_TOKEN,
            "phones": ','.join(phones),
            "content": content,
        }
        requests.post(TELAPI_SMS_URL, data=data)
    except Exception as e:
        print "Some error occurred while sending SMS:", e

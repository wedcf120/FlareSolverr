import time
import re
import os
import json

html = os.system ("sudo python src/flaresolverr.py & sleep 20 && curl  'http://localhost:8191/v1' -H 'Content-Type: application/json' --data '{  \"cmd\": \"request.get\",  \"url\":\"https://sharemania.us/\",  \"maxTimeout\": 60000}'")

data = json.loads(html)           # 解析 JSON 数据
response = data.get('response')   # 获取 response 数据
print(response)                   # 输出 response 数据

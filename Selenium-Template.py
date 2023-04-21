import time
import re
import os
import json
import subprocess

# 启动 subprocess，运行 src/flaresolverr.py 脚本
subprocess.Popen(['sudo', 'python', 'src/flaresolverr.py'])

html = os.system ("sleep 20 && curl  'http://localhost:8191/v1' -H 'Content-Type: application/json' --data '{  \"cmd\": \"request.get\",  \"url\":\"https://sharemania.us/\",  \"maxTimeout\": 60000}'")
print(html)
data = json.loads(html)           # 解析 JSON 数据
response = data.get('response')   # 获取 response 数据
print(response)                   # 输出 response 数据

# -*- coding: UTF-8 -*- 
import time
import re
import os
import json
import subprocess
from datetime import datetime

#subprocess.Popen(['sudo', 'python', 'src/flaresolverr.py'])

# 睡眠 20 秒以确保 flaresolverr.py 已经启动
time.sleep(36)

# 使用 subprocess 模块调用 curl 命令，并捕获命令输出结果
curl_cmd = "curl 'http://localhost:8191/v1' -H 'Content-Type: application/json' --data '{\"cmd\": \"request.get\",\"url\":\"https://javgg.net/new-post\",\"maxTimeout\": 60000, \"proxy\": { \"url\": \"http://127.0.0.1:1085\" }}'"
result = subprocess.check_output(curl_cmd, shell=True)

# 解析 JSON 数据
data = json.loads(result.decode('utf-8'))
response = data.get("solution", {}).get("response")
#print(response)  # 输出 response 数据

with open('./javgg.html', 'w', encoding='utf-8') as f:
       f.write(response)

# 使用 subprocess 模块调用 curl 命令，并捕获命令输出结果
curl_cmd = "curl 'http://localhost:8191/v1' -H 'Content-Type: application/json' --data '{\"cmd\": \"request.get\",\"url\":\"https://supjav.com/category/censored-jav\",\"maxTimeout\": 60000, \"proxy\": { \"url\": \"http://127.0.0.1:1085\" }}'"
result = subprocess.check_output(curl_cmd, shell=True)

# 解析 JSON 数据
data = json.loads(result.decode('utf-8'))
response = data.get("solution", {}).get("response")
#print(response)  # 输出 response 数据

with open('./supjav-censored.html', 'w', encoding='utf-8') as f:
       f.write(response)

os.system("pkill chrome; pkill chromedriver")

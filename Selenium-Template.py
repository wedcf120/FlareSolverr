# -*- coding: UTF-8 -*- 
import time
import re
import os
import json
import subprocess


subprocess.Popen(['sudo', 'python', 'src/flaresolverr.py'])

# 睡眠 20 秒以确保 flaresolverr.py 已经启动
time.sleep(32)

# 使用 subprocess 模块调用 curl 命令，并捕获命令输出结果
curl_cmd = "curl -s 'http://localhost:8191/v1' -H 'Content-Type: application/json' --data '{\"cmd\": \"request.get\",\"url\":\"https://sharemania.us/\",\"maxTimeout\": 60000}'"
result = subprocess.check_output(curl_cmd, shell=True)

# 解析 JSON 数据
data = json.loads(result.decode('utf-8'))
response = data.get("solution", {}).get("response")
#print(response)  # 输出 response 数据

pattern = r'href\=\"(threads\/.+?)\"\>'
links = re.findall(pattern, response)

print (links)

html_string = ""

for link in links[:3]:
    url = "https://sharemania.us/" + link
    print(url)
    os.system("pkill chrome;pkill chromedriver")
    curl_cmd = "curl -s 'http://localhost:8191/v1' -H 'Content-Type: application/json' --data '{\"cmd\": \"request.get\",\"url\":\"" + url + "\",\"maxTimeout\": 60000}'"
    result = subprocess.check_output(curl_cmd, shell=True)
    data = json.loads(result.decode('utf-8'))
    response = data.get("solution", {}).get("response")
    html_string += response

print(html_string)

with open('./sharemania.html', 'w', encoding='utf-8') as f:
    f.write(html_string)

# -*- coding: UTF-8 -*- 
import time
import re
import os
import sys
import json
import subprocess
from datetime import datetime

#subprocess.Popen(['sudo', 'python', 'src/flaresolverr.py'])

# 睡眠 20 秒以确保 flaresolverr.py 已经启动
time.sleep(36)

#判断代理有没有用
os.system("curl --proxy 127.0.0.1:1085 https://proapi.115.com/app/uploadinfo")

# 使用 subprocess 模块调用 curl 命令，并捕获命令输出结果
curl_cmd = "curl 'http://localhost:8191/v1' -H 'Content-Type: application/json' --data '{\"cmd\": \"request.get\",\"url\":\"" + sys.argv[1] + "\",\"maxTimeout\": 60000, \"proxy\": { \"url\": \"http://127.0.0.1:1085\" }}'"
result = subprocess.check_output(curl_cmd, shell=True)


# 解析 JSON 数据
data = json.loads(result.decode('utf-8'))
response = data.get("solution", {}).get("response")
print(response)  # 输出 response 数据


# 使用正则表达式从结果中提取图片地址
pattern = r'https://img\.supjav\.com/images/.+?\.(jpg|png|bmp)'
matches = re.finditer(pattern, result)
for match in matches:
    img_url = match.group()
    # 构建第二个 curl 命令来下载图片
    img_filename = img_url.split('/')[-1]
    curl_cmd_2 = f"curl 'http://localhost:8191/v1' -H 'Content-Type: application/json' --data '{{\"cmd\": \"request.get\",\"url\":\"{img_url}\",\"maxTimeout\": 60000, \"proxy\": {{ \"url\": \"http://127.0.0.1:1085\" }} }}' > {img_filename}"
    subprocess.run(curl_cmd_2, shell=True)
    os.system("pkill chrome; pkill chromedriver")


os.system("pkill chrome; pkill chromedriver")

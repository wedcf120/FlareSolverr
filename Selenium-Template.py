import time
import re
import os
import json
import subprocess

# 启动 subprocess，运行 src/flaresolverr.py 脚本
subprocess.Popen(['sudo', 'python', 'src/flaresolverr.py'])

time.sleep(20)  # 等待 20 秒以确保 flaresolverr.py 已经启动

# 使用 subprocess 模块调用 curl 命令，并捕获命令输出结果
curl_cmd = "curl -s 'http://localhost:8191/v1' -H 'Content-Type: application/json' --data '{\"cmd\": \"request.get\",\"url\":\"https://sharemania.us/\",\"maxTimeout\": 60000}'"
result = subprocess.check_output(curl_cmd, shell=True)

# 解析 JSON 数据
data = json.loads(result.decode('utf-8'))
response = data.get('response')
print(response)  # 输出 response 数据

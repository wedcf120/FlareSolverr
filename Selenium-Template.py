import time
import re
import os

html = os.system ("sudo sudo python src/flaresolverr.py & sleep 5 ; curl  'http://localhost:8191/v1' -H 'Content-Type: application/json' --data '{  \"cmd\": \"request.get\",  \"url\":\"https://sharemania.us/\",  \"maxTimeout\": 60000}'")
print (html);

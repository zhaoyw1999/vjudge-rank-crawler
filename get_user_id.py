import json

from urllib.request import urlopen

import re
import requests
from bs4 import BeautifulSoup

def get_id_str(s):
    p = 0
    ret = ''
    for x in s:
        if ord(x) >= ord('0') and ord(x) <= ord('9'):
            ret = ret + x
    return ret

with open('origin.json', 'r') as f:
    data = json.load(f)
f.close()

for i in range(0, len(data)):
    if data[i]['vjudge_account'] != '$NULL':
        url = 'https://vjudge.net/user/' + data[i]['vjudge_account']
        html = urlopen(url).read().decode('UTF-8')
        soup = BeautifulSoup(html, features='lxml')
        content_list = soup.find_all(text=re.compile('\(#\d{4,6}\)'))
        data[i]['vjudge_id'] = get_id_str(content_list[0])
        print(data[i]['student_name'], get_id_str(content_list[0]))
    else:
        data[i]['vjudge_id'] = '$NULL'
        print(data[i]['student_name'], '$NULL')

with open('acmer.json', 'w') as f:
    json.dump(data, f)
f.close()
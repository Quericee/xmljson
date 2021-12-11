import xml.etree.ElementTree as ET
from urllib.request import urlopen
import json

data = urlopen('https://lenta.ru/rss').read().decode('utf8')
root = ET.fromstring(data)
result = []
for item in root.findall("channel/item"):
    rec = {}
    for tag in item:
        rec[tag.tag] = tag.text
    result.append(rec)

with open("news2.json", "w", encoding='utf8') as write_file:
    json.dump(result, write_file, ensure_ascii=False)

#!usr/bin/env python
# coding: utf-8

import requests
from bs4 import BeautifulSoup

r = requests.get('http://210.35.251.243/opac/search.php')
# r.encoding = 'ISO-8859-1'
# r.encoding = 'gbk'

page = r.content

s = r.content
soup = BeautifulSoup(s)
t = s.decode('utf-8')
with open('log.txt', 'w') as foo:
	foo.write(t.encode('utf-8'))

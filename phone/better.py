# coding:utf-8

from bs4 import BeautifulSoup
import requests
import re


def add_list(line):
    blank = re.compile('\s+')
    container = []
    for i in line:
        m = blank.match(str(i))
        if not m:
            container.append(i)
    return container


def add_dict(line):
    mainlist = add_list(line[1])
    length = len(line)
    c = []
    for i in range(2, length):
        l = add_list(line[i])
        d = {}
        for index, j in enumerate(l):
            d[mainlist[index].string] = j.string.strip('\n\t\r')
        c.append(d)
    return c


def print_item(c):
    for i in c:
        for j, v in i.items():
            print j, v


class Main():

    def __init__(self):
        response = requests.get('http://www.ncu.edu.cn/zydt/xyhy.htm')
        soup = BeautifulSoup(response.content, "html.parser")
        line = soup.find_all('tr')
        self.mainli = add_dict(line)
        self.title = add_list(line[1])

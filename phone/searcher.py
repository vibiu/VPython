# coding:utf-8

from better import Main
from better import print_item
import re

def print_phone(phonedict):
    print phonedict[keyword[0]]+phonedict[keyword[1]],':','-'.join([phonedict[keyword[2]],phonedict[keyword[3]]])

mainkey = Main()
keyword = [i.string for i in mainkey.title]
for i in keyword:
    print i
phone = mainkey.mainli
searchword = raw_input('>')
searchword = unicode(searchword,'gbk')
word = re.compile(searchword)
k = []
for i in phone:
    for key,values in i.items():
        if word.match(values):
            k.append(i)
if k:
    for i in k:
        print_phone(i)

else:
    print 'not find'


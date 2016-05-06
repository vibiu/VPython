# coding:utf-8

import requests
import HTMLParser


def decoder(url):
    htmldecoder = HTMLParser.HTMLParser()
    response = requests.get(url)
    content = response.content.decode('utf-8')
    page = htmldecoder.unescape(content)
    return page


def spliter(page, left, right):
    aList = page.split(left)
    bList = []
    for i in aList:
        bList.append(i.split(right)[0])
    bList.pop(0)
    return bList

url = 'http://210.35.251.243/opac/ajax_top_lend_shelf.php'
page = decoder(url)
hrefs = spliter(page, 'href="', '"><span>')
books = spliter(page, '<span>', '</span')

mainList = []
for i in range(10, 20):
    mainList.append([])
    mainList[i - 10].append(books[i])
    mainList[i - 10].append('http://210.35.251.243/opac/' + hrefs[i])

# mainList 中就是books的列表，mainList中的元素第一个是书名，第二个是书的网页地址
#eg. mainList[0][0] = "百年孤独"; mainList[0][1] = "'http://210.35.251.243/opac/item.php?marc_no=0000431036"

# you can do this to check out!
if __name__ == '__main__':
    for i in mainList:
    print i[0], '-' * 20, i[1]

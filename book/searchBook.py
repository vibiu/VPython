# coding: utf-8

from books import mainList, decoder, spliter


def check(searchword):
    searchword = searchword.decode('utf-8')
    for i in mainList:
        if searchword in i[0]:
            return i[1]
    return False


def farmatag(htmlstr, tag):
    if tag in htmlstr:
        tempList = htmlstr.split(tag)
        tlist = tempList[0].split('>')
        htmlstr = tlist[1] + tempList[1]
    return htmlstr


def search(keyword):
    url = check(keyword)
    if url:
        page = decoder(url)
        emphasize = spliter(page, '<dt>', '</dd>')
        freeList = []
        for i, v in enumerate(emphasize):
            if i != len(emphasize) - 1 and i != len(emphasize) - 2:
                bookitem = v.split('</dt>\r\n\t\t\t\t\t\t\t\t\t<dd>')
                freeList.append([])
                freeList[i].append(bookitem[0])
                freeList[i].append(farmatag(bookitem[1], '</a>'))
        return freeList
    else:
        return None


def scrapy(keyword):
    if search(keyword):
        for i in search(keyword):
            print i[0], i[1]
    else:
        print 'not find'

# you can test it like this
if __name__ == '__main__':
    keyword = '新概念英语词汇练习'
    scrapy(keyword)

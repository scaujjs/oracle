#coding:utf-8

import time
import socket
none_known="none known"
Bronze="BronzeImages"
Oracle="OracleImages"
import os
import sys
import urllib
import urllib2
from urllib2 import URLError
from lxml import etree
reload(sys)
sys.setdefaultencoding( "utf-8" )
import re


## here are some parameter you must make it correct bofore you run the code
repositoryAdd="C:\\Users\\Angus\\PycharmProjects\\ocracle\\repository"



def spider(character):
    src=u"http://www.chineseetymology.org/CharacterEtymology.aspx?characterInput="+character+"&submitButton1=Etymology"

    while(True):
        try:
            response = urllib2.urlopen(src,timeout=10)
            html = response.read()
            break
        except Exception, e:
            print "try to reconnect"



    page_source = etree.HTML(html.decode('utf-8'))

    if not os.path.exists(repositoryAdd+"\\"+character):
        os.makedirs(repositoryAdd+"\\"+character)

    (exisanceOfB,numOfB )=taskOftype(page_source,Bronze,character)
    (exisanceOfO, numOfO)=taskOftype(page_source,Oracle,character)
##    print(repr(stringOfBronze).decode('unicode-escape'))
##    print(repr(stringOfOcracle).decode('unicode-escape'))
    return (exisanceOfB,numOfB,exisanceOfO,numOfO)

def taskOftype(page_source,Bronze,character):
    exisance=True
    num=0
    base="/html/body/table//span[@id='"+Bronze+"']"
    result=page_source.xpath(base+"//pre//text()")
    strings=''
    for string in result:
        strings=strings+string

##    print(repr(strings).decode('unicode-escape'))
    if(none_known in strings):
        exisance=False

    if exisance:
        namesOfPic = base + \
                     "//tr//td[@style='background-color: rgb(237, 226, 203)']/text()"
        resultsOfName = page_source.xpath(namesOfPic)
        hrefOfBronzePic = base + \
                          "//tr//td//img/@src"
        resultOfPicSrc = page_source.xpath(hrefOfBronzePic)
        assert len(resultsOfName)==len(resultOfPicSrc)
        num=len(resultsOfName)

        for i in range(num):
            resultsOfName[i]=resultsOfName[i].strip()

##        print(repr(resultsOfName).decode('unicode-escape'))
##        print(repr(resultOfPicSrc).decode('unicode-escape'))

        downloader(character,Bronze,resultsOfName,resultOfPicSrc)

    return (exisance,num)

def writein2log(a):
    file = 'C:\\Users\\Angus\\PycharmProjects\\ocracle\\log.txt'
    b = a.encode('utf')
    f = open(file, "a")
    f.write(b)
    f.close()

def downloader(character,type,namesOfPic,resultOfPicSrc):
    base="http://www.chineseetymology.org"
    letter=''
    if type==Bronze:
        letter='bronze'
    if type==Oracle:
        letter='oracle'
    if not os.path.exists(repositoryAdd + u"\\"+character+"\\"+letter):
        os.makedirs(repositoryAdd + u"\\"+character+"\\"+letter)
    add=repositoryAdd + u"\\"+character+"\\"+letter
    for i in range(len(namesOfPic)):
        url=base+resultOfPicSrc[i]
        path=add+"\\"+namesOfPic[i]+".jpg"
        if not os.path.exists(path):
            ##urllib.urlretrieve(url, path)
            while (True):
                try:
                    fp = urllib2.urlopen(url, timeout=5)
                    break
                except Exception,e:
                    print "try to reconnect pic "+str(namesOfPic[i])


            data = fp.read()
            # 清除并以二进制写入
            f = open(path, 'w+b')
            f.write(data)
            f.close()

''''
start=time.time()
(exisanceOfB, numOfB, exisanceOfO, numOfO)=spider(u"\u8F66")
identify ='8f66'
hanzi = u'\u8f66'
print identify
print hanzi
line =identify+','+ \
      repr(hanzi).decode('unicode-escape') +','+str(exisanceOfB)+','+str(numOfB)+','+str(exisanceOfO)+','+str(numOfO)+'\n'
print line
writein2log(line)
end=time.time()
print (end-start)



'''

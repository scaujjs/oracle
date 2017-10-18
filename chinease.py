#coding:utf-8

import time

import sys
import downloader
reload(sys)
sys.setdefaultencoding( "utf-8" )




start=19968
end=40960

def startScrapy(init):
    start = 19968
    end = 40960
    numOfWord = 0
    numOfBPic = 0
    numOfOpic = 0
    starttime = time.time()

    try:
        for i in range(init, end):
            identify = '\u' + (hex(i)).replace('0x', '')

            hanzi = identify.decode('unicode-escape')

            (exisanceOfB, numOfB, exisanceOfO, numOfO) = downloader.spider(hanzi)
            line = identify + ',' + \
                   hanzi + ',' + str(exisanceOfB) + ',' + str(numOfB) + ',' + str(
                exisanceOfO) + ',' + str(numOfO) + '\n'
            print line
            numOfWord = numOfWord + 1
            numOfBPic = numOfBPic + numOfB
            numOfOpic = numOfOpic + numOfO
            downloader.writein2log(line)
    finally:
        end = time.time()
        last = end - starttime
        print "last: " + str(last)
        print "numOfWord: " + str(numOfWord)
        print "numOfBPic: " + str(numOfBPic)
        print "numOfOPic: " + str(numOfOpic)







startScrapy(20821)
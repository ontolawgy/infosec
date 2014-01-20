#!/usr/bin/env python
#Copyright AMH, 2013. MIT licensed (i.e., attribution please,
#but do what you want with it and don't sue me)
#See LICENSE
#Inspired by https://xkcd.com/936 and https://www.grc.com/haystack.htm
#Usage: xckdpass-mod.py [number of words] [padding length]

import random
import os, re, sys
from sys import argv

def getargs():
    if len(argv) == 3:
        numwords = argv[1]
        numpads = argv[2]
        return(numwords, numpads)
    elif len(argv) == 2:
        numwords = argv[1]
        numpads = 4
        return (numwords, numpads)
    else:
        numwords = 2
        numpads = 4
        return (numwords, numpads)

def dicopen(dictionary="/usr/share/dict/american-english"):
    f = open(dictionary, "r")
    dic = f.readlines()
    return dic

def genPassword(numwords, numpads):
    r = random.SystemRandom()
    pads = '0123456789!@#$%^&*()'
    padding = []
    words = dicopen()
    wordlist = []
    for i in range (0,int(numpads)):
        padding.append(pads[r.randint(0,len(pads)-1)])
    j = 0
    while (j < int(numwords)):
        inclusion_criteria = re.compile('^[a-z]{4,8}$')
        cur = words[r.randint(0,len(words)-1)].strip()
        if inclusion_criteria.match(cur):
            wordlist.append(cur)
            j += 1
        else:
            pass
    return(" ".join(wordlist)+' '+''.join(padding))

if(__name__ == "__main__"):
    for i in range (1,11):
       print "item "+str(i)+"\n"+genPassword(getargs()[0], getargs()[1])

# coding=utf-8
from urllib import urlopen
from bs4 import BeautifulSoup
from urllib import quote
import  sys
import codecs
import json
def printChineseCodes():
    start,end = (0x4E00, 0x9FA5)
    with codecs.open("chinese.txt", "wb", encoding="utf-8") as f:
        for codepoint in range(int(start),int(end)):
            print(unichr(codepoint).encode('utf8'),)
            f.write(unichr(codepoint))
#"http://m.hmz.com/xmcs/%BB%AA_%CE%E4%D0%C7_%B9%AB%C0%FA%202017%C4%EA6%D4%C21%C8%D57%CA%B1_%C4%D0/"
def loopChineses():
    start,end = (0x4E00, 0x9FA5)
    names  = []
    with codecs.open("names.txt", "wb", encoding="utf-8") as f:
        for codepoint in range(int(start),int(end)):
            code=unichr(codepoint)
            url="http://m.hmz.com/xmcs/%BB%AA_%CE%E4{0}_%B9%AB%C0%FA%202017%C4%EA6%D4%C21%C8%D57%CA%B1_%C4%D0/".format( quote(code.encode('gbk')))
            scores =getGoodName(url)
            if(scores<>None):
                oneName={"name":"华武"+code.encode("utf8"),"五格":scores[0],"八字":scores[1]}
                jsonName = json.dumps(oneName, ensure_ascii=False, encoding='UTF-8')
                print jsonName
                f.write(jsonName)
                names.append(code)
    print names
def loop2():
    url = "http://m.hmz.com/xmcs/%BB%AA_{0}_%B9%AB%C0%FA%202017%C4%EA6%D4%C21%C8%D57%CA%B1_%C4%D0/".format(
        quote(code.encode('gbk')))
    scores = getGoodName(url)
    if (scores <> None and ((scores[0] == scores[1]) or (scores[0] == 100 and scores[1] > 90) or (
            scores[1] == 100 and scores[0] > 90))):
        oneName = {"姓名": "华" + code.encode("utf8"), "五格": scores[0], "八字": scores[1]}
        jsonName = json.dumps(oneName, ensure_ascii=False, encoding='UTF-8')
        print("{0}/{1}:".format(i, iSize))
        print jsonName
        f.write(jsonName)
        names.append(code)
    url="http://m.hmz.com/xmcs/%BB%AA_{0}%CE%E4_%B9%AB%C0%FA%202017%C4%EA6%D4%C21%C8%D57%CA%B1_%C4%D0/".format( quote(code.encode('gbk')))
    scores =getGoodName(url)
    if(scores<>None and((scores[0]==scores[1] and scores[0]>90) or( scores[0]==100 and scores[1]>85) or( scores[1]==100 and scores[0]>85))):
        oneName={"姓名":"华"+code.encode("utf8")+"武","五格":scores[0],"八字":scores[1]}
        jsonName = json.dumps(oneName, ensure_ascii=False, encoding='UTF-8')
        print("{0}/{1}:".format(i,iSize))
        print jsonName
        f.write(jsonName)
        names.append(code)
def loopChineses2():
    start, end = (0x4E00, 0x9FA5)
    names = []
    i=0
    iSize=len(range(int(start), int(end)))
    with codecs.open("names.txt", "wb", encoding="utf-8") as f:
        for codepoint in range(int(start), int(end)):
            i+=1
            code = unichr(codepoint)

            url="http://m.hmz.com/xmcs/%BB%AA_%CE%E4{0}_%B9%AB%C0%FA%202017%C4%EA6%D4%C21%C8%D57%CA%B1_%C4%D0/".format( quote(code.encode('gbk')))
            scores =getGoodName(url)
            if(scores<>None and((scores[0]==scores[1] and scores[0]>90) or( scores[0]==100 and scores[1]>85) or( scores[1]==100 and scores[0]>85))):
                oneName={"姓名":"华武"+code.encode("utf8"),"五格":scores[0],"八字":scores[1]}
                jsonName = json.dumps(oneName, ensure_ascii=False, encoding='UTF-8')
                print("{0}/{1}:".format(i, iSize))
                print jsonName
                f.write(jsonName)
                names.append(code)

    print names

def getGoodName(url):
    try:
        html = urlopen(url)
    except HTTPError:
        return None
    try:
        bsObj = BeautifulSoup(html)
        overScore =False
        result=[]
        nameList = bsObj.find_all("span", {"class": "redred"})
        for name in nameList:
            score=float(name.get_text())
            result.append(score)
            if(score>=90):
                overScore = True
    except:
        return None

    if(overScore):
        return  result
    else:
        return None
#getGoodName("http://m.hmz.com/xmcs/%BB%AA_%CE%E4%D0%C7_%B9%AB%C0%FA%202017%C4%EA6%D4%C21%C8%D57%CA%B1_%C4%D0/")
loopChineses2()
#printChineseCodes()





def test():
    oneName = {"name": "华武" + unichr(0x4E00).encode("utf8"), "五格": 1, "八字": 2}
    print oneName
    print oneName["name"]
    jsonName = json.dumps(oneName, ensure_ascii=False, encoding='UTF-8')
    print  jsonName
    with codecs.open("chinese.txt", "wb", encoding="utf-8") as f:
        f.write(jsonName)
    #print(quote("编码坑爹"))
    #print("编码坑爹".decode("gbk").encode("utf-8"))
    #print(quote(u"华".encode("utf-8")))
    #print(quote(u"华".encode("gbk")))
    #print(bsObj.title.decode("gbk").encode("utf8"))

#test()


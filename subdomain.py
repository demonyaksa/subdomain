# -*- coding: UTF-8 -*-

import requests,threadpool

url1="http://"
print("输入主域名，例：qq.com")
domain = input()
url2="." + str(domain)

lists=[]


def zd():
    f=open("sub_full.txt",'r')
    for d in f:
        dir=d.strip()
        lists.append(dir)

def bp(str):
    try:
        res=requests.get(url1+str+url2,timeout=5)
        if res.status_code==200:
            print(url1+str+url2)
        elif res.status_code==403:
            print(url1+str+url2)
    except:
        pass
zd()
pool=threadpool.ThreadPool(20)
reqs=threadpool.makeRequests(bp,lists)
[pool.putRequest(req) for req in reqs]
pool.wait()

input("按任意键退出")
# -*- coding: utf-8 -*-
from concurrent.futures import ThreadPoolExecutor
import requests
import json
from nonebot import on_command, CommandSession
from .contents import *
from .discord_webhook import *

# on_command 装饰器将函数声明为一个命令处理器
# 这里 weather 为命令的名字，同时允许使用别名「天气」「天气预报」「查天气」
@on_command('zhanji', aliases=('战绩'),only_to_me=False)
async def zhanji(session):
        await session.send('正在查询')   
        v = ThreadPoolExecutor(5).submit(fetch_async)
        v.add_done_callback(callback(v,session))
        ThreadPoolExecutor(5).shutdown(wait=True)


def fetch_async():
    strloose=""
    for p in PERSON:
        uid = p[0]
        name = p[1]
        try:
            url = "https://api.opendota.com/api/players/{}/recentMatches".format(uid)
            r = requests.get(url)
            if r.ok:
                result = json.loads(r.content.decode('utf-8'))
        except Exception:
            print('战绩查询失败')
        loosenum=0
        winnum=0
        Wflag=0
        Lflag=0
        for match in result:
            win=loosecombo(match)
            if(win==1)and(Wflag==1):
                winnum=winnum+1                           
            if (win==1) and (Wflag==0):#第一把赢
                Wflag=Wflag+1
                Lflag=9
                winnum=winnum+1
            if(win==0)and(Wflag==1):
                Wflag=Wflag+1
    
            if(win==0)and(Lflag==1):
                loosenum=loosenum+1                     
            if(win==0)and(Lflag==0):#第一把输
                Lflag=Lflag+1
                Wflag=9
                loosenum=loosenum+1                    
            if(win==1)and(Lflag==1):
                Lflag=Lflag+1
                    
                
        if Wflag==2:
            Wflag=Wflag+1
            strloose=strloose+'{}已经连胜{}把'.format(name,winnum)+"\n"
        elif Lflag==2:
            Lflag=Lflag+1
            strloose=strloose+'{}已经连跪{}把'.format(name,loosenum)+"\n"    

    return strloose


async def callback(future,session):

    await session.send(future.result())


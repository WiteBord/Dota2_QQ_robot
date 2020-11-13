# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 19:22:48 2020

@author: Administrator
"""

import requests
from nonebot import on_command, CommandSession

@on_command('hhfriend', aliases=('hh有正在打dota的好友吗'),only_to_me=False)
async def hhfriend(session: CommandSession):
    dotanum=0
    dotaname=""
    #拉取好友列表
    url =( "http://api.steampowered.com/ISteamUser/GetFriendList/v0001/"+
        "?key=D53CA9B68F94628EA30DFC43F2B906C1&steamid=76561198310988027&relationship=friend")
    
    r=requests.get(url)
    result=r.json()["friendslist"]["friends"]
    
    await session.send("成功拉取好友列表，共"+str(len(result))+"位，正在逐个核对")
    
    for i in result:
        
        #查询目前状态
        url =( "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/"+
              "?key=D53CA9B68F94628EA30DFC43F2B906C1&steamids="+i["steamid"]+"&relationship=friend")
        r = requests.get(url)
        try:
            if r.json()["response"]["players"][0]["gameextrainfo"]=="Dota 2":
                dotanum+=1
                dotaname+=r.json()["response"]["players"][0]["personaname"]+"\n"
        except:
            pass
    if dotanum==0:
        await session.send("没有哦~")
    else:
        await session.send("现在有"+str(dotanum)+"位好友在打dota，名字为:\n"+dotaname)

# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 19:22:48 2020

@author: Administrator
"""

import requests

#拉取好友列表
#url =( "http://api.steampowered.com/ISteamUser/GetFriendList/v0001/"+
#    "?key=D53CA9B68F94628EA30DFC43F2B906C1&steamid=76561198347384371&relationship=friend")

#查询目前状态
url =( "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/"+
    "?key=D53CA9B68F94628EA30DFC43F2B906C1&steamids=76561198347384371&relationship=friend")
r = requests.get(url)
result = r.json()["response"]["players"][0]["gameextrainfo"]#现在正在玩的游戏
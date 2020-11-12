# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 10:35:40 2020

@author: yy
"""
import random
from nonebot import on_command, CommandSession


# on_command 装饰器将函数声明为一个命令处理器
# 这里 weather 为命令的名字，同时允许使用别名「天气」「天气预报」「查天气」
@on_command('roll',only_to_me=False)
async def roll(session):
    Rnum=random.randint(0,100)
    await session.send(str(Rnum))

@on_command('roll5',only_to_me=False)
async def roll5(session: CommandSession):
    Rstr=''
    Rall=0
    for i in range(0,5):
        Rnum=random.randint(0,100)
        Rall=Rall+Rnum
        Rstr=Rstr+str(Rnum)+' '
    Rstr=Rstr+'\n总和为'+str(Rall)
    await session.send(Rstr)
    
@on_command('roll10',only_to_me=False)
async def roll10(session: CommandSession):
    Rstr=''
    Rall=0
    for i in range(0,10):
        Rnum=random.randint(0,100)
        Rall=Rall+Rnum
        Rstr=Rstr+str(Rnum)+' '
    Rstr=Rstr+'\n总和为'+str(Rall)
    await session.send(Rstr)
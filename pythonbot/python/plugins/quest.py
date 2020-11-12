# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 09:40:00 2020

@author: yy
"""
import random
from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand


@on_natural_language({''}, only_to_me=False)#监测问题并进行回答
async def _(session: NLPSession):
    Que = session.msg_text
    
    if(Que=='quest'):
        global mmr
        mmr=0
    if(mmr!=9999):
        if(Que=='A'):
            mmr=mmr+1
        elif(Que=='B'):
            mmr=mmr+100
        elif(Que!='quest'):
            if(random.randint(1,2)==1):
                await session.send('回答不符合规范，已随机A')
                mmr=mmr+1
            else:
                await session.send('回答不符合规范，已随机B')
                mmr=mmr+100    

    
    if mmr==0:
        await session.send('有人吗？有人能收到消息吗\nA.做出回答  B.置之不理')#A:1,B:100
        
    if mmr==1:
        await session.send('啊啊，我被困在了一个奇怪的地方，左边是条走廊，右边是个山洞，你能帮我选择下往哪里走吗？\nA.左边  B.右边')#A2,B101
    
    if mmr==2:
        await session.send('右边的墙壁上有扇门，我要进去看看吗？\nA.进去   B.不进去')#A3,B102

                
    if mmr==102:
        await session.send('Demo结束')
        mmr=9999    
    if mmr==100:    
        await session.send('求救声逐渐消失，无线电陷入了沉寂')   
        mmr=9999
    if mmr==101:
        await session.send('随着一声惨叫，无线电陷入了沉寂')
        mmr=9999
    if mmr==3:
        await session.send('你听到了慌乱的脚步声和无线电掉落到地板上的声音，随后无线电中只剩下信号受到干扰后的杂音，你与对方失去了联系')
        mmr=9999
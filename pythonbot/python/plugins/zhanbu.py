# -*- coding: utf-8 -*-
#from nonebot import on_command, CommandSession
from nonebot.experimental.plugin import on_command,CommandSession
from nonebot.experimental.permission import simple_allow_list
from .contents import HEROES_LIST_CHINESE,HEROES_NAME
import random
import numpy as np
import time

day='00-00'

allow_list = simple_allow_list(group_ids={1056465127}, reverse=False)

def xipai():
    global zhanbu
    zhanbu=np.zeros((119,5))
    for i in range(119):
        for j in range(5):
            zhanbu[i][j]=random.randint(0,100)
    global rowsum
    rowsum=np.sum(zhanbu,axis=1)
    

@on_command('zhanbuxipai', aliases=('洗牌'),only_to_me=False,permission=allow_list)
async def zhanbuxipai(session: CommandSession):
    xipai()
    await session.send("占卜洗牌完成")
    

@on_command('Czhanbu', aliases=('占卜'),only_to_me=False,permission=allow_list)
async def Czhanbu(session: CommandSession):
    global day
    if (day!=time.strftime("%m-%d", time.localtime())):
        day=time.strftime("%m-%d", time.localtime())       
        await session.send("这是本日第一次占卜，进行洗牌")
        xipai()
        
    heros = session.get('target', prompt='你想占卜哪个英雄呢？')
    zhanbu_result = await get_zhanbu_of_heros(heros)

    await session.send(zhanbu_result)


@Czhanbu.args_parser
async def _(session: CommandSession):
    # 去掉消息首尾的空白符
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        # 该命令第一次运行（第一次进入命令会话）
        if stripped_arg:
            # 第一次运行参数不为空，意味着用户直接将城市名跟在命令名后面，作为参数传入
            # 例如用户可能发送了：天气 南京
            session.state['target'] = stripped_arg
        return

    if not stripped_arg:
        # 用户没有发送有效的城市名称（而是发送了空白字符），则提示重新输入
        # 这里 session.pause() 将会发送消息并暂停当前会话（该行后面的代码不会被运行）
        session.pause('要占卜的英雄名称不能为空呢，请重新输入')

    # 如果当前正在向用户询问更多信息（例如本例中的要查询的城市），且用户输入有效，则放入会话状态
    session.state[session.current_key] = stripped_arg


async def get_zhanbu_of_heros(heros: str) -> str:
    # 这里简单返回一个字符串
    strresult=''
    
    if heros=='最优':
        addmaxidx = (-rowsum).argsort()[:3]#最大
        for i in range(3):
            strresult=(strresult+HEROES_LIST_CHINESE[addmaxidx[i]][0]+':\n'+
                   '对线'+str(zhanbu[addmaxidx[i]][0])+
                   '刷钱'+str(zhanbu[addmaxidx[i]][1])+
                   '切入'+str(zhanbu[addmaxidx[i]][2])+
                   '团战'+str(zhanbu[addmaxidx[i]][3])+
                   '大菊观'+str(zhanbu[addmaxidx[i]][4])+'\n')
            
    elif heros=='最差':
        addminidx = (rowsum).argsort()[:3]#最小
        for i in range(3):
            strresult=(strresult+HEROES_LIST_CHINESE[addminidx[i]][0]+':\n'+
                   '对线'+str(zhanbu[addminidx[i]][0])+
                   '刷钱'+str(zhanbu[addminidx[i]][1])+
                   '切入'+str(zhanbu[addminidx[i]][2])+
                   '团战'+str(zhanbu[addminidx[i]][3])+
                   '大菊观'+str(zhanbu[addminidx[i]][4])+'\n')        
    else:
        index=np.where(HEROES_LIST_CHINESE==heros)
        if index[0].size==0:
            strresult='无法找到需要占卜的英雄'
        else:    
            strresult=(heros+':\n'+
                   '对线'+str(zhanbu[index[0][0]][0])+
                   '刷钱'+str(zhanbu[index[0][0]][1])+
                   '切入'+str(zhanbu[index[0][0]][2])+
                   '团战'+str(zhanbu[index[0][0]][3])+
                   '大菊观'+str(zhanbu[index[0][0]][4]))
    
    return strresult
    
@on_command('herorandom5', aliases=('全英雄随机5'),only_to_me=False,permission=allow_list)
async def herorandom5(session: CommandSession):
    heroid=np.zeros(5)
    heronum=0
    strhero=''
    for i in range(10):
        randhero=random.randint(0,118)
        index=np.where(heroid==randhero)
        if(index[0].size==0):
            heroid[heronum]=randhero
            strhero=strhero+HEROES_NAME[randhero]+' ' 
            heronum=heronum+1
            if(heronum==5):
                break  

    await session.send(strhero)  
    
@on_command('herorandom10', aliases=('全英雄随机10'),only_to_me=False,permission=allow_list)
async def herorandom10(session: CommandSession):
    heroid=np.zeros(10)
    heronum=0
    strhero=''
    for i in range(30):
        randhero=random.randint(0,118)
        index=np.where(heroid==randhero)
        if(index[0].size==0):
            heroid[heronum]=randhero
            strhero=strhero+HEROES_NAME[randhero]+' ' 
            heronum=heronum+1
            if(heronum==10):
                break  

    await session.send(strhero)     
    

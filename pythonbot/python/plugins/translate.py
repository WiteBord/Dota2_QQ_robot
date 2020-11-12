# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 15:36:32 2020

@author: Administrator
"""
import requests
import hashlib

from nonebot import on_command, CommandSession

@on_command('translate', aliases=('#'),only_to_me=False)
async def translate(session: CommandSession):

    q = session.get('q', prompt='请输入待翻译语句')
    
    #lista=q.split()
    #q=q.replace(lista[0]+" "+lista[1]+" ","")
    appid="20201106000609772"
    key="oX_ZDn9G1Thl7UC7mWuy" 
    salt="1435660288"
    sign=hashlib.md5((appid+q+salt+key).encode(encoding='utf-8')).hexdigest()
    url = "http://api.fanyi.baidu.com/api/trans/vip/translate?q="+q+"&from=auto&to=zh"+\
    "&appid="+appid+"&salt="+salt+"&sign="+sign
    r = requests.get(url)
    result = r.json()

    await session.send(result['trans_result'][0]['dst'])

@translate.args_parser
async def _(session: CommandSession):
  
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['q'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('要翻译的语句不能为空呢，请重新输入')
    session.state[session.current_key] = stripped_arg









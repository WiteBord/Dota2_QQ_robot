# -*- coding: utf-8 -*-
import os
import random
from nonebot import on_command, CommandSession,MessageSegment 


@on_command('picture', aliases=('图片'),only_to_me=False)
async def picture(session: CommandSession):
    fileword = session.get('fileword', prompt='你想找哪个人物的图片呢？')
    picnum=random.randint(0,len(os.listdir('./' + fileword))-1)
    picname=os.listdir('./' + fileword)[picnum]
    
    picture=MessageSegment.image(f'C:\\pythonbot\\{fileword}\\{picname}')
    
    await session.send(picture)
    
    
@picture.args_parser
async def _(session: CommandSession):
    # 去掉消息首尾的空白符
    stripped_arg = session.current_arg_text.strip()
    if session.is_first_run:
        if stripped_arg:
            session.state['fileword'] = stripped_arg
        return
    if not stripped_arg:
        session.pause('要查询的名称不能为空呢，请重新输入')
    session.state[session.current_key] = stripped_arg
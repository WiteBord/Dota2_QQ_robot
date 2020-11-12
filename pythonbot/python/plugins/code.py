# -*- coding: utf-8 -*-

from nonebot import on_command, CommandSession


@on_command('code',only_to_me=False)
async def roll(session):
    code_text=session.get('code_text',prompt='请输入执行代码')
    result=str(eval(code_text))
    await session.send(result)

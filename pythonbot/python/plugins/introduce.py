# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 19:38:01 2020

@author: yy
"""

from nonebot import on_command, CommandSession

@on_command('introduce',aliases=('介绍', '功能介绍'),only_to_me=False)
async def introduce(session):
    await session.send('本机器人可提供:\n'+
                       '1.dota连胜/连败查询指令:战绩查询\n'+
                       '2.天气查询指令:天气 地名\n'+
                       '3.ROLL点指令:roll,roll5,roll10\n'+
                       '4.QA存储指令:QA 问题 回答\n'+
                       '5.翻译指令:#\n'+
                       '6.英雄占卜指令(需先使用“洗牌”指令)：占卜 英雄名/占卜 最优/占卜 最差/全英雄随机5/全英雄随机10\n'+
                       '7.预测胜率指令：预测 A-B-C-D-E-F-G-H-I-J  前5个为天辉，后5个为夜魇  本功能由15756场全英雄训练3层神经网络所得模型构建，不保证准确度，仅供娱乐'+
                       '8.击剑指令：剑术大师赛(需2人)')
    
    
    
@on_command('why',aliases=('为什么'),only_to_me=False)
async def why(session:CommandSession):
    Ques = session.get('Ques', prompt='你想询问什么问题呢？')
    
    await session.send(Ques+'是怎么回事呢？'+Ques+'相信大家都很熟悉，但是'+Ques+'是怎么回事呢，下面就让小编带大家一起了解吧。'+Ques+
                       '，其实就是'+Ques+'，大家可能会很惊讶'+Ques+'怎么会是'+Ques+'呢？但事实就是这样，小编也感到非常惊讶。这就是关于'+
                       Ques+'的事情了，大家有什么想法呢，欢迎在评论区告诉小编一起讨论哦！')
    
    await session.send()    
    
    
@why.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if session.is_first_run:
        if stripped_arg:
            session.state['Ques'] = stripped_arg
        return
    if not stripped_arg:
        session.pause('要查询问题不能为空呢，请重新输入')
    session.state[session.current_key] = stripped_arg    
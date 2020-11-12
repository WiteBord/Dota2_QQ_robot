# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 12:29:45 2020

@author: yy
"""
from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand

#from nonebot.experimental.plugin import on_command,CommandSession,on_natural_language, NLPSession, IntentCommand
#from nonebot.experimental.permission import simple_allow_list

question=[]
answer=[]



@on_command('QandA', aliases=('QA'),only_to_me=False)
async def QandA(session: CommandSession):
    # 从会话状态（session.state）中获取城市名称（city），如果当前不存在，则询问用户
    QA = session.get('QA', prompt='请输入问题与回答')
    
    if(QA.find(' ')!=0):
        preque=QA[0:QA.find(' ')]
        #判断QA表中是否已经存在
        if(question.count(preque)!=0):#问题已经存在
            index=question.index(preque)
            answer[index]=QA[QA.find(' ')+1:]
            await session.send('答案已覆盖')
        else:#问题还未存在
            question.append(QA[0:QA.find(' ')])
            answer.append(QA[QA.find(' ')+1:])
            await session.send('设置完成')

    #await session.send(question[0])
    #await session.send(answer[0])


@QandA.args_parser
async def _(session: CommandSession):
    # 去掉消息首尾的空白符
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        # 该命令第一次运行（第一次进入命令会话）
        if stripped_arg:
            # 第一次运行参数不为空，意味着用户直接将城市名跟在命令名后面，作为参数传入
            # 例如用户可能发送了：天气 南京
            session.state['QA'] = stripped_arg
        return

    if not stripped_arg:
        # 用户没有发送有效的城市名称（而是发送了空白字符），则提示重新输入
        # 这里 session.pause() 将会发送消息并暂停当前会话（该行后面的代码不会被运行）
        session.pause('问答不能为空呢，请重新输入')

    # 如果当前正在向用户询问更多信息（例如本例中的要查询的城市），且用户输入有效，则放入会话状态
    session.state[session.current_key] = stripped_arg

@on_command('AtoQ',aliases=('回答'),only_to_me=False)#问题前需要带“回答”命令，目前不采用
async def AtoQ(session: CommandSession):
    Que = session.get('Que', prompt='请输入问题')
    if(question.count(Que)!=0):
        index=question.index(Que)
        await session.send(answer[index])
               
@on_natural_language({''}, only_to_me=False)#监测问题并进行回答
async def _(session: NLPSession):
    Que = session.msg_text
    if(question.count(Que)!=0):
        index=question.index(Que)
        await session.send(answer[index])
        
       

@AtoQ.args_parser
async def _(session: CommandSession):
    # 去掉消息首尾的空白符
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        # 该命令第一次运行（第一次进入命令会话）
        if stripped_arg:
            # 第一次运行参数不为空，意味着用户直接将城市名跟在命令名后面，作为参数传入
            # 例如用户可能发送了：天气 南京
            session.state['Que'] = stripped_arg
        return

    if not stripped_arg:
        # 用户没有发送有效的城市名称（而是发送了空白字符），则提示重新输入
        # 这里 session.pause() 将会发送消息并暂停当前会话（该行后面的代码不会被运行）
        session.pause('问题不能为空呢，请重新输入')

    # 如果当前正在向用户询问更多信息（例如本例中的要查询的城市），且用户输入有效，则放入会话状态
    session.state[session.current_key] = stripped_arg
    
    
@on_command('QALIST', aliases=('QA表'),only_to_me=False)#列出QA表的内容
async def QALIST(session):
    QAstr=''
    if(len(question)==0):
        await session.send('QA表为空')
    for i in range(len(question)):
        QAstr=QAstr+question[i]+' ==>> '+answer[i]+'\n'
    await session.send(QAstr)

@on_command('QAclean', aliases=('清理QA表'),only_to_me=False)#清除QA表的内容
async def QAclean(session):
    question.clear()
    answer.clear()       
    await session.send('清理完成')

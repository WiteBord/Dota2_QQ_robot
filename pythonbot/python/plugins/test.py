# -*- coding: utf-8 -*-
from contents import *
from discord_webhook import *

# on_command 装饰器将函数声明为一个命令处理器
# 这里 weather 为命令的名字，同时允许使用别名「天气」「天气预报」「查天气」



strloose=""        
uid =141354095
name ='小雪堆'
try:
    open_dota_matches_refresh(uid)
    result = get_recent_matches(uid)
    loosenum=0
    winnum=0
    Wflag=0
    Lflag=0
    for match in result:
        win=loosecombo(match)
        print(win)
        if(win==1)and(Wflag==1):
            winnum=winnum+1   
            print('a')                        
        elif (win==1) and (Wflag==0):#第一把赢
            Wflag=Wflag+1
            Lflag=9
            winnum=winnum+1
            print('b')  
        elif(win==0)and(Wflag==1):
            Wflag=Wflag+1
            print('c')  

        if(win==0)and(Lflag==1):
            loosenum=loosenum+1
            print('d')                       
        elif(win==0)and(Lflag==0):#第一把输
            Lflag=Lflag+1
            Wflag=9
            loosenum=loosenum+1 
            print('e')                     
        elif(win==1)and(Lflag==1):
            Lflag=Lflag+1
            print('f')  
                
                    
        if Wflag==2:
            Wflag=Wflag+1
            strloose=strloose+'{}已经连胜{}把'.format(name,winnum)+"\n"
        elif Lflag==2:
            Lflag=Lflag+1
            strloose=strloose+'{}已经连跪{}把'.format(name,loosenum)+"\n"
except Exception:
    print('error')
print(strloose)
        
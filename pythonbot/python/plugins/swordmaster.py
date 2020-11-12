# -*- coding: utf-8 -*-
import random
from nonebot import on_command,CommandSession,on_natural_language, NLPSession

p1name=""
p2name=""
firstname=""
secondname=""
p1hp=20
p2hp=20
flag=1 
f1rd=0
f2rd=0
restart=0
healrd1=0
healrd2=0
@on_natural_language({''}, only_to_me=False)#监测问题并进行回答
async def _(session: NLPSession):
    global p1name
    global p2name
    global p1hp
    global p2hp
    global flag
    global f1rd
    global f2rd
    global firstname
    global secondname
    global restart
    global healrd1
    global healrd2
       
    if session.msg_text=="剑术大师赛":
        if p1name=="":
            p1name=str(session.ctx['sender']['nickname'])
            await session.send(p1name+"向群内各位发出击剑邀请！")
        elif p2name=="":
            p2name=str(session.ctx['sender']['nickname'])
            await session.send(p2name+"接受了"+p1name+"发出的击剑邀请！")           
           
    if p1name!="" and p2name!="" and flag==1:        
        await session.send("剑术大师赛开始！") 
#####################先攻判定#####################################
        while flag:        
            atknum1=random.randint(1,20)
            atknum2=random.randint(1,20)
            if atknum1>atknum2:
                await session.send(p1name+"先攻掷骰(1d20)："+str(atknum1)+"\n"\
                                   +p2name+"先攻掷骰(1d20)："+str(atknum2)+"\n"+p1name+"先攻！")
                await session.send("攻击方式说明：\n1 力量型攻击，伤害1d16，命中率25%\n"+\
                                   "2 敏捷型攻击，伤害1d8,命中率75%\n"+\
                                   "3 治疗术，每回合回血1d6,持续3回合")
                flag=0
                firstname=p1name
                secondname=p2name
            elif atknum1<atknum2:
                await session.send(p1name+"先攻掷骰(1d20)："+str(atknum1)+"\n"\
                                   +p2name+"先攻掷骰(1d20)："+str(atknum2)+"\n"+p2name+"先攻！")
                await session.send("攻击方式说明：\n1 力量型攻击，伤害1d16，命中率25%\n"+\
                                   "2 敏捷型攻击，伤害1d8,命中率75%"+\
                                   "3 治疗术，每回合回血1d6,持续3回合")
                flag=0
                firstname=p2name
                secondname=p1name
########################################################################
    if f1rd==1 and f2rd==1:
        f1rd=0
        f2rd=0
        
        if healrd1!=0 and healrd2!=0:
            healrd1=healrd1-1
            heal1=random.randint(1,6)
            p1hp=p1hp+heal1 
            if p1hp>20:
                p1hp=20
            healrd2=healrd2-1
            heal2=random.randint(1,6)
            p2hp=p2hp+heal2  
            if p2hp>20:
                p2hp=20
            await session.send("*回合初结算*\n"+firstname+"治疗术掷骰(1d6):"+str(heal1)+
                               "\n"+secondname+"治疗术掷骰(1d6):"+str(heal2)+
                           "\n"+firstname+"剩余生命为:"+str(p1hp)+
                           "\n"+secondname+"剩余生命为:"+str(p2hp))        
        elif healrd1!=0:
            healrd1=healrd1-1
            heal1=random.randint(1,6)
            p1hp=p1hp+heal1
            if p1hp>20:
                p1hp=20
            await session.send("*回合初结算*\n"+firstname+
                               "治疗术掷骰(1d6):"+str(heal1)+
                           "\n"+firstname+"剩余生命为:"+str(p1hp)+
                           "\n"+secondname+"剩余生命为:"+str(p2hp))
            
        elif healrd2!=0:    
            healrd2=healrd2-1
            heal2=random.randint(1,6)
            p2hp=p2hp+heal2   
            if p2hp>20:
                p2hp=20
            await session.send("*回合初结算*\n"+secondname+
                               "治疗术掷骰(1d6):"+str(heal2)+
                           "\n"+firstname+"剩余生命为:"+str(p1hp)+
                           "\n"+secondname+"剩余生命为:"+str(p2hp))
        
########################################################################        
    if session.ctx['sender']['nickname']==secondname and f1rd==1 and f2rd==0:
        if(session.msg_text=="1"):
            f2rd=1
            hit=random.randint(1,20)
            if hit<16:
                await session.send(secondname+"命中掷骰(1d20):"+str(hit)+"<16,未命中"+\
                                   "\n"+firstname+"剩余生命为:"+str(p1hp)+
                                    "\n"+secondname+"剩余生命为:"+str(p2hp))
            elif hit==20:
                damage1=random.randint(1,16)
                damage2=random.randint(1,16)
                p1hp=p1hp-damage1-damage2
                await session.send(secondname+"命中掷骰(1d20):"+str(hit)+\
                                   "=20,重击\n伤害掷骰1(1d16):"+str(damage1)+\
                                    "\n伤害掷骰2(1d16):"+str(damage2)+\
                                    "\n"+firstname+"剩余生命为:"+str(p1hp)+
                                    "\n"+secondname+"剩余生命为:"+str(p2hp))
            else:
                damage1=random.randint(1,16)
                p1hp=p1hp-damage1
                await session.send(secondname+"命中掷骰(1d20):"+str(hit)+\
                                   "\n伤害掷骰(1d16):"+str(damage1)+\
                                    "\n"+firstname+"剩余生命为:"+str(p1hp)+
                                    "\n"+secondname+"剩余生命为:"+str(p2hp))        
        elif(session.msg_text=="2"):
            f2rd=1
            hit=random.randint(1,20)
            if hit<=5:
                await session.send(secondname+"命中掷骰(1d20):"+str(hit)+"<=5,未命中"+\
                                   "\n"+firstname+"剩余生命为:"+str(p1hp)+
                                    "\n"+secondname+"剩余生命为:"+str(p2hp))
            elif hit==20:
                damage1=random.randint(1,8)
                damage2=random.randint(1,8)
                p1hp=p1hp-damage1-damage2
                await session.send(secondname+"命中掷骰(1d20):"+str(hit)+\
                                   "=20,重击\n伤害掷骰1(1d8):"+str(damage1)+\
                                    "\n伤害掷骰2(1d8):"+str(damage2)+\
                                    "\n"+firstname+"剩余生命为:"+str(p1hp)+
                                    "\n"+secondname+"剩余生命为:"+str(p2hp))
            else:
                damage1=random.randint(1,8)
                p1hp=p1hp-damage1
                await session.send(secondname+"命中掷骰(1d20):"+str(hit)+\
                                   "\n伤害掷骰(1d8)"+str(damage1)+\
                                    "\n"+firstname+"剩余生命为:"+str(p1hp)+
                                    "\n"+secondname+"剩余生命为:"+str(p2hp))
        elif(session.msg_text=="3"):
            f2rd=1
            healrd2=2
            heal=random.randint(1,6)
            p2hp=p2hp+heal
            if p2hp>20:
                p2hp=20
            await session.send(secondname+"治疗术掷骰(1d6):"+str(heal)+\
                               "\n"+firstname+"剩余生命为:"+str(p1hp)+
                               "\n"+secondname+"剩余生命为:"+str(p2hp))
        else:
            f2rd=0
        
########################################################################            
    if session.ctx['sender']['nickname']==firstname and f1rd==0:
        if(session.msg_text=="1"):
            f1rd=1
            hit=random.randint(1,20)
            if hit<=15:
                await session.send(firstname+"命中掷骰(1d20):"+str(hit)+"<=15,未命中"+\
                                    "\n"+firstname+"剩余生命为:"+str(p1hp)+
                                    "\n"+secondname+"剩余生命为:"+str(p2hp))
                                  
            elif hit==20:
                damage1=random.randint(1,16)
                damage2=random.randint(1,16)
                p2hp=p2hp-damage1-damage2
                await session.send(firstname+"命中掷骰(1d20):"+str(hit)+\
                                   "=20,重击\n伤害掷骰1(1d16):"+str(damage1)+\
                                    "\n伤害掷骰2(1d16):"+str(damage2)+\
                                    "\n"+firstname+"剩余生命为:"+str(p1hp)+
                                    "\n"+secondname+"剩余生命为:"+str(p2hp))
            else:
                damage1=random.randint(1,16)
                p2hp=p2hp-damage1
                await session.send(firstname+"命中掷骰(1d20):"+str(hit)+\
                                   "\n伤害掷骰(1d16):"+str(damage1)+"\n"+\
                                    "\n"+firstname+"剩余生命为:"+str(p1hp)+
                                    "\n"+secondname+"剩余生命为:"+str(p2hp))
        elif(session.msg_text=="2"):
            f1rd=1
            hit=random.randint(1,20)
            if hit<=5:
                await session.send(firstname+"命中掷骰(1d20):"+str(hit)+"<=5,未命中"+\
                                    "\n"+firstname+"剩余生命为:"+str(p1hp)+
                                    "\n"+secondname+"剩余生命为:"+str(p2hp))
                                  
            elif hit==20:
                damage1=random.randint(1,8)
                damage2=random.randint(1,8)
                p2hp=p2hp-damage1-damage2
                await session.send(firstname+"命中掷骰(1d20):"+str(hit)+\
                                   "=20,重击\n伤害掷骰1(1d8):"+str(damage1)+\
                                    "\n伤害掷骰2(1d8):"+str(damage2)+\
                                    "\n"+firstname+"剩余生命为:"+str(p1hp)+
                                    "\n"+secondname+"剩余生命为:"+str(p2hp))
            else:
                damage1=random.randint(1,8)
                p2hp=p2hp-damage1
                await session.send(firstname+"命中掷骰(1d20):"+str(hit)+\
                                   "\n伤害掷骰(1d8):"+str(damage1)+"\n"+\
                                    "\n"+firstname+"剩余生命为:"+str(p1hp)+
                                    "\n"+secondname+"剩余生命为:"+str(p2hp))
        elif(session.msg_text=="3"):
            f1rd=1
            healrd1=2
            heal=random.randint(1,6)
            p1hp=p1hp+heal
            if p1hp>20:
                p1hp=20
            await session.send(firstname+"治疗术掷骰(1d6):"+str(heal)+\
                               "\n"+firstname+"剩余生命为:"+str(p1hp)+
                               "\n"+secondname+"剩余生命为:"+str(p2hp))
        else:
            f1rd=0
######################################################################## 
 



######################################################################## 
    if p1hp<=0:
        await session.send(secondname+"为本次剑术大师赛胜者！")
        restart=1
    elif p2hp<=0:
        await session.send(firstname+"为本次剑术大师赛胜者！")
        restart=1
    
    if restart==1:
        p1name=""
        p2name=""
        firstname=""
        secondname=""
        p1hp=20
        p2hp=20
        flag=1 
        f1rd=0
        f2rd=0
        restart=0
        
    
    
    
            
        

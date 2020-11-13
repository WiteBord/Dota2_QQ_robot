# Dota2_QQ_robot
## 本机器人使用 [MiraiOK](https://github.com/LXY1226/MiraiOK) + [cqhttp-mirai](https://github.com/yyuueexxiinngg/cqhttp-mirai) + [nonebot](https://github.com/nonebot/nonebot)  构建，用于dota2群内 ~~整蛊VCD看回蓝~~ 和谐交流
整个流程为**MiraiOK**收到消息，通过**cqhttp-mirai插件**发给**nonebot**处理，处理完成后将结果通过**cqhttp-mirai插件**传给**MiraiOK**进行发送，机器人的各种功能由**nonebot**来负责实现
## pythonbot/plugins 文件夹内文件为实现各种功能的代码,各种功能实现所调用的api详见[nonebot开发文档](https://docs.nonebot.dev/)
**nonebot**启动方式：在cmd界面输入`python bot.py`

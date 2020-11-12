#from nonebot import on_command,CommandSession
from nonebot import on_command,CommandSession
from nonebot.command import kill_current_session




@on_command('privilege_kill', privileged=True,only_to_me=False)
async def _(session: CommandSession):
    kill_current_session(session.event)
    await session.send('已强制关闭当前正在运行的会话')
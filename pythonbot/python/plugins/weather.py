import requests###导入网络请求包2
from xpinyin import Pinyin
from nonebot import on_command, CommandSession


# on_command 装饰器将函数声明为一个命令处理器
# 这里 weather 为命令的名字，同时允许使用别名「天气」「天气预报」「查天气」
@on_command('weather', aliases=('天气', '天气预报', '查天气'),only_to_me=False)
async def weather(session: CommandSession):
    # 从会话状态（session.state）中获取城市名称（city），如果当前不存在，则询问用户
    city = session.get('city', prompt='你想查询哪个城市的天气呢？')
    # 获取城市的天气预报
    weather_report = await get_weather_of_city(city)
    # 向用户发送天气预报
    await session.send(weather_report)


# weather.args_parser 装饰器将函数声明为 weather 命令的参数解析器
# 命令解析器用于将用户输入的参数解析成命令真正需要的数据
@weather.args_parser
async def _(session: CommandSession):
    # 去掉消息首尾的空白符
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        # 该命令第一次运行（第一次进入命令会话）
        if stripped_arg:
            # 第一次运行参数不为空，意味着用户直接将城市名跟在命令名后面，作为参数传入
            # 例如用户可能发送了：天气 南京
            session.state['city'] = stripped_arg
        return

    if not stripped_arg:
        # 用户没有发送有效的城市名称（而是发送了空白字符），则提示重新输入
        # 这里 session.pause() 将会发送消息并暂停当前会话（该行后面的代码不会被运行）
        session.pause('要查询的城市名称不能为空呢，请重新输入')

    # 如果当前正在向用户询问更多信息（例如本例中的要查询的城市），且用户输入有效，则放入会话状态
    session.state[session.current_key] = stripped_arg


async def get_weather_of_city(city: str) -> str:
    # 这里简单返回一个字符串
    # 实际应用中，这里应该调用返回真实数据的天气 API，并拼接成天气预报内容
    p=Pinyin()
    Pcity=p.get_pinyin(city,'')#中文改拼音
    try:
        url='http://api.openweathermap.org/data/2.5/weather?q='+Pcity+'&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996' 
        rst=requests.get(url).json()#获取json数据
        a1=rst['main']['temp']
        a2=rst['weather'][0]['description']
        a3=rst['wind']['speed']
        a4=rst['main']['temp_min']
        a5=rst['main']['temp_max']
        a6=rst['main']['humidity']
        a7=rst['sys']['country']
        a8=rst['coord']['lon']
        a9=rst['coord']['lat']
        strweather=(str(a7)+'-'+city+'\n经度'+str(a8)+' 纬度'+str(a9)+
                    '\n当前温度:'+str(a1)+'°C 天气情况:'+str(a2)+'\n'+
                    '最低温度:'+str(a4)+'°C '+'最高温度:'+str(a5)+'°C'+
                    '\n风速:'+str(a3)+'           湿度:'+str(a6))
        return strweather
    except Exception as e:
        return f'找不到“{city}”的天气'
    
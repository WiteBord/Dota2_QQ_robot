# -*- coding: utf-8 -*-
from nonebot import on_command, CommandSession,MessageSegment 
import os
import re
import urllib.request, urllib.error, urllib.parse
import urllib
import _thread
import time
import socket
import json
import shutil

def SaveImage(url, path):   # 传入的url是图片url地址
    request = urllib.request.Request(url)   # 模拟浏览器头部信息
    request.add_header('accept','image/webp,image/apng,*/*;q=0.8')
    request.add_header('accept-encoding','gzip, deflate, br')
    request.add_header('accept-language','zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6')
    request.add_header('sec-fetch-dest','image')
    #request.add_header('sec-fetch-mode','no-cors')
    #request.add_header('sec-fetch-site','cross-site')
    request.add_header('referer','https://pixivic.com/popSearch')
    request.add_header('user-agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36')
    try:
        response = urllib.request.urlopen(request)  # 打开该url得到响应
        img = response.read()   # read读取出来
        f = open(path, 'wb')    # 以二进制写入的格式打开
        f.write(img)    # 写入
        f.close()       # 关闭
    except urllib.error.URLError as ue:  # 捕获urlerror
        if hasattr(ue, 'code'):  # 如果ue中包含'code'字段, 则打印出来
            print(ue.code)
        if hasattr(ue, "reason"):# 如果ue中包含'reason'字段, 则打印出来
            print(ue.reason)
    except IOError as ie:
        print(ie)

    return 




class Crawler:
    __time_sleep = 0.1  # 延时时间
    __counter = 0       # 正在保存的第几个计数
    __start_amount = 0  # 开始页码
    __amount = 0        # 总页码
    headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}

    # 构造函数
    def __init__(self, t, word):    # word为想查找图片的名字字段
        self.__time_sleep = t
        if os.path.exists("./" + word):
            shutil.rmtree("./" + word)    #递归删除文件夹
            
        if not os.path.exists("./" + word):     # 检测是否存在该word文件夹, 不存在则创建
            os.mkdir("./" + word)
        
        self.__counter = len(os.listdir('./' + word)) + 1   # 返回word路径下所有条目的信息, 并加一     

    # 获取后缀
    def get_suffix(self, name):     # name为保存图片时传入的网址
        m = re.search(r'\.[^\.]*$', name)   # \. 表示匹配.而不是任意字符
                                            # [^\.]*$ 表示匹配除了.之外的所有字符,0到n个并以其结尾
        if m.group(0) and len(m.group(0)) <= 5: # m.group(0)表示匹配到的第一个元素
            return m.group(0)   # 如果第一个元素存在, 并长度小于5, 则返回
        else:                   # 否则返回 '.jpeg'
            return '.jpeg'

    # 保存图片
    def save_image(self, rsp_data, word):
        for image_info in rsp_data['imageUrls']:
            try:    # 有可能发生异常的代码片段
                # 替换链接片段
                pps = image_info['original'].replace('https://i.pximg.net/','https://original.img.cheerfun.dev/')
                # print(pps) # 打印图片真实链接
                suffix = self.get_suffix(pps)
                #time.sleep(1)
                # 保存图片
                # 开启一个新线程, 并传入执行的函数, 与对应参数, 参数为图片url与保存的文件名
                _thread.start_new_thread(SaveImage, (pps, './' + word + '/' + str(self.__counter) + str(suffix)))
            except urllib.error.HTTPError as http_err:
                print(http_err) # 出现HTTPError打印其信息, 并继续往下执行
                continue
            except Exception as e:  # 出现其他错误, 休眠一秒, 打印其信息, 并继续往下执行
                time.sleep(2)
                print(e)
                print("出现未知错误, 放弃保存") 
                continue
            else:   # 没发生异常时执行的语句
                sum = len(os.listdir('./' + word))  # 查询当前word字段文件夹下的文件个数
                # print(f'第{str(self.__counter)}张涩图正在保存, 已有{str(sum)}张涩图') # Python3.6新引入的一种字符串格式化方法, 大括号{}标明被替换的字段
                # 文本框的打印输出
                print('end', f'第{str(self.__counter)}张涩图正在保存, 已有{str(sum)}张涩图, 保存在{os.getcwd()}下的{word}文件夹\n')
                if(sum>=50):
                    return
                # if(self.__counter%10==0):                    
                #     global session
                #     await session.send('第{str(self.__counter)}张涩图正在保存, 已有{str(sum)}张涩图')
                
                
                self.__counter += 1 # 保存完一张后将counter计数加一
                time.sleep(self.__time_sleep)   # 并延时指定的秒数
        return
        
    
    # 获取图片
    def get_image(self, word=''):
        search = urllib.parse.quote(word) # 转义替换路径中的 / 
        pagenum = self.__start_amount   # 获取开始页码
        while pagenum <= self.__amount: # 当开始页码小于总页码时循环    
            url = 'https://api.pixivic.com/illustrations?keyword='+search+'&page='+str(pagenum)   # 写入url
            # print(url)  # 打印url
            try:
                req = urllib.request.Request(url=url, headers=self.headers)     # 用户代理, 告诉浏览器我们可以接受什么水平的信息
                page = urllib.request.urlopen(req)      # 接受打开url返回的信息
                rsp = page.read().decode('utf-8')       # 读取接受到的page信息并以utf-8格式保存到rsp中
            except UnicodeDecodeError as e: # 当在编码过程中发生与 Unicode 相关的错误
                print(e)
                print('-----UnicodeDecodeErrorurl:', url)
            except urllib.error.URLError as e: # urlerror
                print(e)
                print("-----urlErrorurl:", url)
            except socket.timeout as e: # 响应超时
                print(e)
                print("-----socket timout:", url)
            else:
                rsp_data = json.loads(rsp)   # 使用此conversion table将包含JSON文档的s（a str实例）解压缩为Python对象。
                temp = rsp_data['data']      # 将返回的data存入, 并在下方遍历传入save_image中, 再在data中提取出图片链接
                for ele in temp:    # 下载一页的图片
                    self.save_image(ele, word)  
                print("下载下一页")
                pagenum += 1
            finally:
                page.close() # 关闭
        print("下载结束")
        # await session.send('下载结束')
        return


    def start(self, word, page_num, start_page):    # 开始
        self.__start_amount = start_page    # 开始页码
        self.__amount = page_num            # 总页码
        self.get_image(word)                # 获取图片




# on_command 装饰器将函数声明为一个命令处理器
# 这里 weather 为命令的名字，同时允许使用别名「天气」「天气预报」「查天气」
@on_command('crawl', aliases=('爬'),only_to_me=False)
async def crawl(session: CommandSession):
    
    word = session.get('word', prompt='你想找哪个人物的图片呢？')
    
    await session.send("开始爬取，请耐心等待")
    
    
    crawler = Crawler(1.3, word) # 新建一个对象, 并初始化传入延时的时间, 以及想要查找的字段
    crawler.start(word, 1, 1) # 总页码10, 开始页码1
    
    #picture=MessageSegment.image('C:\\Users\\Administrator\\Desktop\\img001.JPG')
    
    await session.send(f"爬取结束,共下载{str(len(os.listdir('./' + word)))}张图片")
    
    
@crawl.args_parser
async def _(session: CommandSession):
    # 去掉消息首尾的空白符
    stripped_arg = session.current_arg_text.strip()
    if session.is_first_run:
        if stripped_arg:
            session.state['word'] = stripped_arg
        return
    if not stripped_arg:
        session.pause('要查询的名称不能为空呢，请重新输入')
    session.state[session.current_key] = stripped_arg
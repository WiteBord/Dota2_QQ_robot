# coding=utf-8
import time


# 输入秒级的时间，转出正常格式的时间
# 10位时间戳
def timeStamp(timeNum):
    timeStamp = float(timeNum)
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return otherStyleTime

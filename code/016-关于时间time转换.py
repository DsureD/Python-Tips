import time
import datetime

timestamp = time.time()    # time.time()获取时间戳数1645766388.2346916(秒)，int(time.time()*1000)获取时间戳整数(毫秒)

# timestamp = 1645766388
print(timestamp)

date_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(timestamp)) # 把时间戳按指定格式输出，如 2022-02-25 13:19:48
print(date_time)
print(datetime.datetime.fromtimestamp(timestamp))  # 把时间戳按指定格式输出，如 2022-02-25 13:19:48.046557

# 把 2022-02-11 11:03:36 转换成时间戳1644548616
print(int(time.mktime(time.strptime('2022-02-11 11:03:36', '%Y-%m-%d %H:%M:%S'))))


print(datetime.datetime.now())  # 获取当前日期和时间  2022-03-03 20:50:46.671774
print(datetime.date.today())    # 获取当前日期   2022-03-24

tomorrow = datetime.date.today() + datetime.timedelta(days=1)   # 日期加减，这个表示前面的日期加或者减days天（正加，负号减）
print(tomorrow,type(str(tomorrow)))

print(time.localtime())  # time.struct_time(tm_year=2022, tm_mon=3, tm_mday=3, tm_hour=20, tm_min=52, tm_sec=13, tm_wday=3, tm_yday=62, tm_isdst=0)
t = time.localtime() # 当前结构化时间
year = t.tm_year  # 提取结构化时间的年份，依此类推tm_mon,tm_mday,tm_hour,tm_min...
print(time.localtime()[0])  # 2022

'''
当前时间2022年3月22日12点21分
time.strftime('%Y-%m-%d %X')            显示 2022-03-22 12:22:56
time.strftime('%Y-%m-%d %H:%M:%S')      显示 2022-03-22 12:22:56
time.strftime('%X')                     显示 12:22:56
time.strftime('%D')                     显示 03/22/22
time.strftime('%y')                     显示 22
time.strftime('%Y')                     显示 2022
time.strftime('%p')                     显示 PM
'''
res = time.strftime('%H:%M:%S')
print(type(res),res)
res2 = time.strftime('%Y-%m-%d')
print(res2)
formatted_date = time.strftime('%Y%m%d%H%M%S')
print(formatted_date)

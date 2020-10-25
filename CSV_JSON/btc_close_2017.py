import json
import pygal
import math
#加载数据
filename = 'btc_close_2017.json'
with open(filename) as f:
    btc_data = json.load(f)
#创建五个列表
dates=[]
months=[]
weeks=[]
weekdays=[]
closes=[]
#打印每一天的信息
for btc_dict in btc_data:
    date = btc_dict['date']
    month = int(btc_dict['month'])
    week = int(btc_dict['week'])
    weekday = btc_dict['weekday']
    close = int(float(btc_dict['close']))
    dates.append(date)
    months.append(month)
    weeks.append(week)
    weekdays.append(weekday)
    closes.append(close)
    #print("{} is month {} week {},{},the close price is {} RMB".format(date,month,week,weekday,close))

line_chart = pygal.Line(x_label_rotation=20,show_minor_x_labels=False)
line_chart.title = '收盘价（RMB）'
line_chart.x_labels = dates
N = 20 #每隔20天显示一次
line_chart.x_labels_major = dates[::N]
#对close中所有元素取对数
closes_log = [math.log10(_) for _ in closes]
line_chart.add('收盘价',closes_log)
line_chart.render_to_file('收盘价对数折线图(RMB).svg')

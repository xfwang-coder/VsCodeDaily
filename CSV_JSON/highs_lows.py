import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    #print(header_row)

    dates,highs = [], []
    lows = []
    #遍历数据中的每一行，从第二行有数据开始
    for row in reader:
        try:
            current_date = datetime.strptime(row[0],"%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date,'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    #根据数据绘制图像
    fig = plt.figure(dpi=128,figsize=(10,6))
    plt.plot(dates,highs,c = 'red',alpha=0.5)
    plt.plot(dates,lows,c='blue',alpha=0.5)
    plt.fill_between(dates,highs,lows,facecolor='green',alpha=0.5)

    #设置图形格式
    plt.title("Daily high and low temperatures,2014",fontsize = 24)
    plt.xlabel('',fontsize=10)
    #将横坐标设置为斜体
    fig.autofmt_xdate()
    plt.ylabel("Temperature(F)",fontsize=8)
    plt.tick_params(axis='both',which='major',labelsize=14)

    plt.show()

    
    #print(highs)
    """for index,clomn_header in enumerate(header_row):
        print(index,clomn_header)"""
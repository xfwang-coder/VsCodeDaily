from die import Die
import pygal

#创建一个六面骰子
die = Die(6)

#初始化结果
results = []
#投掷多次
drop_num = 4000
for roll_num in range(drop_num):
    result = die.roll()
    results.append(result)

#分析结果
frequencies = []
for value in range(1,die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#print(frequencies)
#对结果可视化
hist = pygal.Bar()

title_str = "Results of rolling one D6 " + str(drop_num) + " times"
hist.title = title_str
hist.x_labels = ['1','2','3','4','5','6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6',frequencies)
hist.render_to_file('die_visual.svg')

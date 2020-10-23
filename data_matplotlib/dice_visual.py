from die import Die
import pygal


die_1 = Die(6)
die_2 = Die(10)
#初始化结果
results = []
#投掷多次
drop_num = 4000
for roll_num in range(drop_num):
    result = die_1.roll() + die_2.roll()
    results.append(result)

#分析结果
max_result = die_1.num_sides + die_2.num_sides
frequencies = []
for value in range(2,max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#print(frequencies)
#对结果可视化
hist = pygal.Bar()

title_str = "Results of rolling one D6 " + str(drop_num) + " times"
hist.title = title_str
hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D10',frequencies)
hist.render_to_file('dice_visual.svg')
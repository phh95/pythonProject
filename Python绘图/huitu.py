# 绘制简单的折线图

import matplotlib.pyplot as plt

# 更改图表的样式，使用内置的其他图表样式
# plt.style.use('seaborn')

input_values = [1, 2, 3, 4, 5]  # 传递输入值，即 x 坐标的值
squares = [1, 4, 9, 16, 25]   # 输出值，即 y 坐标的值

fig, ax = plt.subplots()

ax.plot(input_values,squares,linewidth = 5)

# 图表的标题
ax.set_title("折线图",fontsize = 24)

# x 轴小标题
ax.set_xlabel("值",fontsize = 14)

# y 轴小标题
ax.set_ylabel("值的平方",fontsize = 14)

# 刻度标记的大小，改变x、y轴刻度标记的字号大小

ax.tick_params(axis='both',labelsize= 14)

plt.show()

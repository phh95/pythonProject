import matplotlib.pyplot as plt

x_value = range(1,1001)
y_value = [x ** 2 for x in x_value] # 这里的 x ** 2 是指 x 的平方

plt.style.use('seaborn')

# seaborn 图表主题不支持中文，因此我们先声明一下使用的中文字体
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']

fig,ax = plt.subplots()

ax.scatter(x_value,y_value,c=y_value,cmap=plt.cm.Blues,s = 10)

# 设置图表标题
ax.set_title("散点图",fontsize = 24)

# x 轴小标题
ax.set_xlabel("值",fontsize = 14)

# y 轴小标题
ax.set_ylabel("值的平方",fontsize = 14)

# 刻度标记的大小，改变x、y轴刻度标记的字号大小

ax.tick_params(axis='both',which='major',labelsize= 14)

# 每个坐标轴的取值范围
ax.axis([0,1100,0,1100000]) # 设定 x、y 轴的最小值和最大值

# plt.show()

plt.savefig('squares_plot.png',bbox_inches='tight')
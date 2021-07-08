# 绘制随机漫步图

import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    rw = RandomWalk()  # 类的实例化
    rw.fill_walk()

    plt.style.use('classic')

    # 调整图表的尺寸
    fig,ax = plt.subplots(figsize=(15,9),dpi=128) # 15,9 分别是图表的长和宽，单位是英寸

    point_numbers = range(rw.num_points)
    # 去除散点默认的黑色轮廓
    ax.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolors='none',s=15)

    # 突出起点
    ax.scatter(0,0,c='green',edgecolors='none',s=100)

    # 突出终点
    ax.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=100)

    # 隐藏坐标轴
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    # 运行一次随机漫步之后，询问你是否还要再漫步一次
    keep_running = input("Make another walk?(y/n): ")
    if keep_running == 'n':
        break


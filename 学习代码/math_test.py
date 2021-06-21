# 计算圆的周长和面积

radius = float(input('请输入圆的半径：'))
zc = 2 * 3.1416 * radius   # 计算周长
mj = 3.1416 * radius ** 2  # 计算面积
area = 3.1416 * radius * radius

print(zc)
print(mj)
print(area)

print('周长：%.2f' % zc)
import numpy as np

# arr1 = np.array([2,3,4])
# print(arr1)
# print(arr1.dtype)
#
# arr2 = np.array([1.2,2.3,3.4])
# print(arr2.dtype)
#
# # 两个列表直接相加
#
# print(arr1 + arr2)
#
# # numpy 定义的数组直接与标量相乘
#
# print(arr2 * 10)
#
# # 定义一个二维数组，其实也称作矩阵
#
# data = [[1,2,3], [4,5,6]]  # 先定义一个嵌套的列表
# arr3 = np.array(data)   # 通过 numpy 将列表转换为矩阵
# print(arr3)

# print(np.zeros((3,5)))
#
# print(np.ones((4,6)))
#
# print(np.empty((2,3,2))) # 创建一个 2*3*2 的三维矩阵，每个位置都为空值



print(np.arange(10))  # 产生从 0 到 9 的数组

arr4 = np.arange(10)

print(arr4[5:8])

arr4[5:8] = 10   # 对切片进行赋值
print(arr4)


arr_slice = arr4[5:8].copy()  # 创建一个副本
arr_slice[:] = 15   # 将副本中的三个元素更改为 15

print(arr_slice)
print(arr4)




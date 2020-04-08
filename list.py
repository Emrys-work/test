# 列表
list1 = ['Google', 'Runoob', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7 ]
print ("list1[0]: ", list1[0])
print ("list2[1:5]: ", list2[1:5])
# 访问列表中的值
list = ['Google', 'Runoob', 1997, 2000]
print ("第三个元素为 : ", list[2])
list[2] = 2001
print ("更新后的第三个元素为 : ", list[2])
# 更新列表
print ("原始列表 : ", list)
del list[3]
print ("删除第四个元素 : ", list)
# 删除列表元素

L=['Google', 'Runoob', 'Taobao']
print(len(L))    # 列表的长度

a = ['a', 'b', 'c'];n = [1, 2, 3]
x = [a,n]
print(x)
print(x[0][1])
# 列表的嵌套，二维列表元素的选取

# 列表函数：len(list),max(list),min(list),list(seq)将元组转换为列表
# 列表的方法：list.append(obj),list.count(obj),list.index(obj),……
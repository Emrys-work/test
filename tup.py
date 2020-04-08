# 元组
tup = ()
# 创建空元组
tup = (50)
print(type(tup))     # 不加逗号，类型为整型
tup = (50,)
print(type(tup))     # 加上逗号，类型为元组

tup1 = ('Google', 'Runoob', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7 )
print ("tup1[0]: ", tup1[0])
print ("tup2[1:5]: ", tup2[1:5])
# 访问元组
tup3 = tup1 + tup2
print (tup3)
# 元组中的元素值是不允许修改的，但我们可以对元组进行连接组合
# 元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组，eg:del tup，此为删除元组tup，后续不可再用tup
print(id(tup))    # 查看元组的内存地址
# 重新赋值的元组 tup，绑定到新的对象了，不是修改了原来的对象

# 元组内置函数：len(tup),max(tup),min(tup),tup(iterable)将可迭代系列转换为元组
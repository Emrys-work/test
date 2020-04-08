# input("简单的输入：")
a = 1;b = 2
# 使用分号(；)来实现多条语句
print(a)
print(b)
print(a,end = "")
print(b)
# 默认输出会换行，end = ""可以实现不换行

# 元组
tuple = ( 'abcd', 786 , 2.23, 'runoob', 70.2  )
tinytuple = (123, 'runoob')
print (tuple)             # 输出完整元组
print (tuple[0])          # 输出元组的第一个元素
print (tuple[1:3])        # 输出从第二个元素开始到第三个元素
print (tuple[2:])         # 输出从第三个元素开始的所有元素
print (tinytuple * 2)     # 输出两次元组
print (tuple + tinytuple) # 连接元组
# 元组（tuple）与数组类似，不同之处在于元组的元素不能修改。
# 修改元组中的元素的操作是非法的
# 可以把字符串看成是一种特殊的元组
tup1 = ()    # 空元组
tup2 = (20,) # 一个元素，需要在元素后添加逗号
# 注意构造包含 0 或 1 个元素的元组的特殊语法规则
a = 1
b = 2.2
c = True
d = 4+2j
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(isinstance(a,int))
# 数据类型的演示
list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
tinylist = [123, 'runoob']
print(list)
print(list[0])
print(list[1:3])
print(list[2:])
print(list * 2)
print(list + tinylist)
# 列表(数组)的截取
a = [1, 2, 3, 4, 5, 6]
a[0] = 9
print(a)
a[2:5] = []    # 将对应的元素值设置为[]
print(a)
# python中的字符串是不可以改变的，而数组中的元素是可以改变的
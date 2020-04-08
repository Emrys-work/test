# 集合
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
# 上为集合，非字典
print(student)    #输出会自动去掉重复的元素
if "tom" in student:
    print("tom在集合中")
else:
    print("tom不在集合中")
# 此为in在判断语句的应用
a = set('abracadabra')
b = set('alacazam')
print(a)
print(a - b)    #a和b的差集
print(a | b)    #a和b的并集
print(a & b)    #a和b的交集
print(a ^ b)    #a和b中不同时存在的元素
# 此为集合set()运算演示
# 可以使用大括号 { } 或者 set() 函数创建集合，\
# 注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。

# 字典
dict = {}
dict["one"] = "1-菜鸟教程"
dict[2] = "2-菜鸟教程"
print(dict)
print(dict["one"]);print(dict[2])
# 字典的创建，输入输出，截取
tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}
print(tinydict.keys())    #输出所有键
print(tinydict.values())    #输出所有值
# 字典类型也有一些内置的函数，例如clear()、keys()、values()等
"""1、字典是一种映射类型，它的元素是键值对。
2、字典的关键字必须为不可变类型，且不能重复。
3、创建空字典使用 { }。"""
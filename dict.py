# 字典
# d = {key1 : value1, key2 : value2 }
# 字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])
# 访问字典里的值
dict['Age'] = 8               # 更新修改 Age
dict['School'] = "菜鸟教程"    # 添加信息 
print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])

# 删除字典中的元素和清空删除字典
# del dict['Name'] # 删除键 'Name'
# dict.clear()     # 清空字典
# del dict         # 删除字典

# 1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
# 2）键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行

# 字典内置函数和方法


print("I love wxl!")
# 第一条语句

if True:
    print("True")
else:
    print("False")
# 同一个代码块的语句必须包含相同的缩进空格数，不一致会导致运行错误

totle = "item_01" + \
        "item_02 "+ \
        "item_03"
# 反斜杠可以实现多行语句，但(),[],{}中的多行语句，不需要使用反斜杠(\)
print("totle")

# 字符串的截取
str = "Runoob"
print(str)
print(str[0:-1])
print(str[0])
print(str[2:])
print(str * 2)   # 字符串的的重复
print(str + " boom")    # 字符串的连接

print('hello\nrunoob')      
# 使用反斜杠(\)+n转义特殊字符

print(r'hello\nrunoob')     
# 在字符串前面添加一个 r，表示原始字符串，不会发生转义
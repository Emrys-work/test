# 字符串的截取
var1 = 'Hello World!'
var2 = "Runoob"
print ("var1[0]: ", var1[0])
print ("var2[1:5]: ", var2[1:5])
# 字符串的更新，截取字符串的一部分并与其他字段拼接
var1 = 'Hello World!'
print ("已更新字符串 : ", var1[:6] + 'Runoob!')
# 字符串运算符
a = "Hello"
b = "Python"
print("a + b 输出结果：", a + b)
print("a * 2 输出结果：", a * 2)
print("a[1] 输出结果：", a[1])
print("a[1:4] 输出结果：", a[1:4]) 
if( "H" in a) :
    print("H 在变量 a 中")
else :
    print("H 不在变量 a 中")
 
if( "M" not in a) :
    print("M 不在变量 a 中")
else :
    print("M 在变量 a 中")
print (r'\n')
print (R'\n')
# 字符串格式化
print ("我叫 %s 今年 %d 岁!" % ('小明', 10))
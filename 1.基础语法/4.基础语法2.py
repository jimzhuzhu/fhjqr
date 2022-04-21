# 了解换行符
# import使用,在程序的最前面就导入
# 用；一行显示多条语句

# 换行符作用是换行显示，不起真正意义上的重启一段
# windows换行符是'\r\n'  ,linux换行符是'\n' ,mac是'\r'
# python 中将换行符统一成 '\n'
import sys
print('我爱\n刘雨霞')
# import 导入，在高级编程语言中，如果想使用某个类或接口，就要使用import来导入
input("\n\n按下 enter 键后退出。\n")
# 使用；在一行显示多个代码语句,但是pep 8 格式规范，不建议
x = 'liuyuxia'
print(x)

# import 和from import使用中的区别
# import somemoudle ,将整个模块导入
# from somemoudle import somefunction, 从某个模块导入某个函数
# from somemoudle import firstfunc,secondfunc, 从某个模块导入多个函数
# from somemoudle import **, 将某个模块全部函数导入

# 课堂练习
import turtle
turtle.pen()
# input练习，加减乘除，str转换成int
a = input('请输入数字a：')
b = input('请输入数字b：')
print(int(a) + int(b))
print(int(a) - int(b))
print(int(a) * int(b))
print(int(a) / int(b))


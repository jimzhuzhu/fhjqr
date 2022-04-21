# 编码格式： 预先规定的方法将文字，数字等对象编成数码信号
# Python默认情况以UTF-8编码，字符串都是unicode字符串
# -*- coding:utf-8 -*-

# 关键字也称为保留字，不能用来作任何标识符名称
# 查看所以关键字方法
# 1.keyword模块
import keyword
print(keyword.kwlist)

# 2.help函数
help('keywords')

# 注释，给人看便于理解你的代码
'''这也是注释，
只是可以写很多行'''
"""这也可以作为注释哦
机器并不会运行，增加程序可读性"""

# 缩进，保证代码整洁，层次清晰的主要手段
# 缩进空格可变，但同一个代码块缩进空格必须一直，否则运行会报错
# 一般情况缩进4个字符为标准
a = input('请输入结果：')
a = int(a)
b = 1
if a > b:
    print('太棒啦')
else:
    print('再试一次')

# 当语句很长，用反斜杠\ 实现多行语句
c = 4
s = a + \
    b + \
    c
print(s)

# 课堂练习1.用print打印所有的关键字
print(False, None, True, '__peg_parser__', 'and', 'as', 'assert', 'async', 'await',
      'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally',
      'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal',
      'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield')

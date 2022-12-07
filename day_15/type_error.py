# Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> print 'hello world'
#   File "<stdin>", line 1
#     print 'hello world'
#     ^^^^^^^^^^^^^^^^^^^
# SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
# >>> print('hellow')
# hellow
# >>> print(mak)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'mak' is not defined. Did you mean: 'max'?
# >>> mak = 10
# >>> print(mak)
# 10
# >>> numbers_str = ['1', '2', '3', '4', '5']  # iterable
# >>> def add_two_nums(x, y):
# ...     return int(x) + int(y)
# ...
# >>> total = reduce(add_two_nums, numbers_str)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'reduce' is not defined
# >>> print(total)    # 15ha
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'total' is not defined
# >>> num = [1,2,3,4,5]
# >>> num[5]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: list index out of range
# >>> import mmmam
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ModuleNotFoundError: No module named 'mmmam'
# >>> import math
# >>> math.PI
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: module 'math' has no attribute 'PI'. Did you mean: 'pi'?
# >>> math.pi
# 3.141592653589793
# >>> users = {'name':'Aman', 'age':20, 'country':'India'}
# >>> users[name]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'name' is not defined
# >>> users
# {'name': 'Aman', 'age': 20, 'country': 'India'}
# >>> users['name']
# 'Aman'
# >>> users['ll']
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'll'
# >>> 5 + True
# 6
# >>> 6 + a
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'a' is not defined
# >>> 6 + '3'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# >>> 4 + float(3)
# 7.0
# >>> 4 + float('3')
# 7.0
# >>> from math import power
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ImportError: cannot import name 'power' from 'math' (unknown location)
# >>> from math import pow
# >>> pow(3,4)
# 81.0
# >>> int('123a')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: invalid literal for int() with base 10: '123a'
# >>> int('123')
# 123
# >>> hex('123a)
#   File "<stdin>", line 1
#     hex('123a)
#         ^
# SyntaxError: unterminated string literal (detected at line 1)
# >>> hex('123a')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'str' object cannot be interpreted as an integer
# >>> hex(123a)
#   File "<stdin>", line 1
#     hex(123a)
#           ^
# SyntaxError: invalid decimal literal
# >>> 1/0
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ZeroDivisionError: division by zero
# >>>
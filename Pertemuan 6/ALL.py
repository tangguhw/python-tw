Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #20102186
>>> #ALL
>>> #List
>>> l20102186=[1, 3, 4, 5]
>>> print(all(l20102186))
True
>>> l20102186=[0, False]
>>> print(all(l20102186))
False
>>> l20102186=[1, 3, 4, 0]
>>> print(all(l20102186))
False
>>> l20102186=[0, False, 5]
>>> print(all(l20102186))
False
>>> 
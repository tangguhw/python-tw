Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #20102186
>>> #ANY
>>> #List
>>> l20102186=[1, 3, 4, 0]
>>> print(any(l20102186))
True
>>> l20102186=[0, False]
>>> print(any(l20102186))
False
>>> l20102186=[]
>>> print(any(l20102186))
False
>>> #String
>>> s20102186="Hello world"
>>> print(any(s20102186))
True
>>> s20102186='000'
>>> print(any(s20102186))
True
>>> s20102186=''
>>> print(any(s20102186))
False
>>> #Dictionaries
>>> d20102186={0:'False'}
>>> print(any(d20102186))
False
>>> d20102186={0:'False', 1:'True'}
>>> print(any(d20102186))
True
>>> d20102186={0:'False', 'False':0}
>>> print(any(d20102186))
True
>>> d20102186={}
>>> print(any(d20102186))
False
>>> d20102186={'0':'False'}
>>> print(any(d20102186))
True
>>> 
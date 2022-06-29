Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #GENERATORS
>>> def cth_generator2186(l):
	total2186 = 0
	for n in l:
		yield total2186
		total2186 += n

		
>>> test_generator2186 = cth_generator2186([10,20,30,40,50])
>>> print(next(test_generator2186))
0
>>> print(next(test_generator2186))
10
>>> print(next(test_generator2186))
30
>>> 
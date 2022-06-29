Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #FUNCTIONS
>>> PI2186=3.141592
>>> print(5*5*PI2186)
78.5398
>>> print(10*10*PI2186)
314.1592
>>> PI2186 = 3.141592
>>> def luas_lingkaran(r2186) :
	return PI2186*r2186*r2186

>>> print(luas_lingkaran(5))
78.5398
>>> print(luas_lingkaran(10))
314.1592
>>> def tambah2186(a2186,b2186,c2186):
	return a2186+b2186+c2186

>>> print(tambah2186(1,2,3))
6
>>> def tambah2186(*bilangan):
	total2186 = 0
	for n in bilangan:
		total2186 += n
	return total2186

>>> print(tambah2186(1,2,3,4,5,6))
21
>>> import math
>>> dir (math)
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']
>>> math.pi
3.141592653589793
>>> def volume2186(r):
	v = (4.0/3.0)*math.pi*r**3
	return v

>>> volume2186(2)
33.510321638291124
>>> def connect2186(**options) :
	conn_params = {
		'host': options.get('host','127.0.0.1'),
		'port': options.get('port','5432'),
		'user': options.get('user',''),
		'pwd': options.get('pwd',''),
		}
	print(conn_params)

	
>>> connect2186()
{'host': '127.0.0.1', 'port': '5432', 'user': '', 'pwd': ''}
>>> connect2186(host='127.0.0.42', port=5433)
{'host': '127.0.0.42', 'port': 5433, 'user': '', 'pwd': ''}
>>> connect2186(port=5431, user='ftii', pwd='nimda')
{'host': '127.0.0.1', 'port': 5431, 'user': 'ftii', 'pwd': 'nimda'}
>>> 
>>> #KONVERSI FUNGSI SEDERHANA
>>> price2186 = 100
>>> final_price1 = price2186*1.2
>>> final_price2 = price2186+price2186/5.0
>>> final_price3 = price2186*(100+20)/100.0
>>> final_price4 = price2186+price2186*0.2
>>> print(final_price1)
120.0
>>> def calculate_price2186_with_vat(price2186, vat):
	return price2186*(100+vat)/100

>>> calculate_price2186_with_vat(200,10)
220.0
>>> 
>>> #MINIMUM
>>> def minimum2186(*n2186):
	if n2186:
		mn = n2186[0]
		for value in n2186[1:]:
			if value < mn:
				mn = value
		print(mn)

		
>>> minimum2186(1, 3, -7, 9)
-7
>>> minimum2186(2, 3, 4, 0, 10)
0
>>> 
>>> #MAKSIMUM
>>> def maksimum2186(*n2186):
	if n2186:
		mk = n2186[0]
		for value in n2186[1:]:
			if value > mk:
				mk = value
		print (mk)

		
>>> maksimum2186(1, 3, -7, 9)
9
>>> maksimum2186(2, 3, 4, 0, 10)
10
>>> 
>>> #MATRIKS
>>> def matrix_mul2186(a2186,b2186):
	return [[sum(i * j for i, j in zip(r, c))
		 for c in zip(*b2186)]for r in a2186]

>>> a2186 = [[1,2], [3,4]]
>>> b2186 = [[5,1], [2,1]]
>>> c = matrix_mul2186(a2186,b2186)
>>> print (c)
[[9, 3], [23, 7]]
>>> 
>>> #UNGUIDED
>>> def rata_rata2186(a2186,b2186):
	return(a2186+b2186)/2

>>> rata_rata2186(200,350)
275.0
>>> def rata_rata2186(a2186,b2186):
	return(a2186+b2186)/2

>>> print(rata_rata2186(200,350))
275.0
>>> def summ2186(a2186,b2186):
	total2186 = 0
	for bil_hasil in list(range(a2186, b2186+1)):
		total2186 = total2186+bil_hasil
	return total2186

>>> summ2186(1,5)
15
>>> 
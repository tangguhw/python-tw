Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> lst_nim=[20102186]
>>> Listku_20102186 = [x for x in range(3,30) if x%2 == 0]
>>> print(Listku_20102186)
[4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
>>> 
>>> lst_nim=[20102186]
>>> bilangan20102186 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
>>> a20102186 = [bilangan20102186[1], bilangan20102186[3], bilangan20102186[5], bilangan20102186[7], bilangan20102186[9]]
>>> b20102186 = [bilangan20102186[0], bilangan20102186[3], bilangan20102186[6], bilangan20102186[9], bilangan20102186[12]]
>>> print(a20102186)
[1, 3, 5, 7, 9]
>>> print(b20102186)
[0, 3, 6, 9, 12]
>>> 
>>> lst_nim = [20102186]
>>> ganjil20102186 = []
>>> subtiga20102186 = []
>>> for n in range(0,13):
	if n%3==0:
		subtiga20102186.append(n)

		
>>> for n in range(0,12):
	if n%2 != 0 and  n != 11:
		ganjil20102186.append(n)

		
>>> print(ganjil20102186)
[1, 3, 5, 7, 9]
>>> print(subtiga20102186)

      
[0, 3, 6, 9, 12]
>>> 
>>> lst_nim = [20102186]
>>> bilangan20102186 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
>>> ganjil20102186 = []
>>> subtiga20102186 = []
>>> for n in bilangan20102186:
	if n%3==0:
		subtiga20102186.append(n)

		
>>> for n in bilangan20102186:
	if n%2 != 0 and  n != 11:
		ganjil20102186.append(n)

		
>>> print(ganjil20102186)
[1, 3, 5, 7, 9]
>>> print(subtiga20102186)
[0, 3, 6, 9, 12]
>>> 
>>> lst_nim = [20102186]
>>> kuadratkan_list_20102186 = []
>>> kuadratkan_dict_20102186 = {}
>>> for i in range (0,10):
	kuadratkan_list_20102186.append(i*i)
	kuadratkan_dict_20102186[i]=i*i

	
>>> print(kuadratkan_list_20102186)
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> print(kuadratkan_dict_20102186)
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
>>> 
>>> nim = [20102186]
>>> inventory20102186 = {
	'emas' : 500,
	'kantong' : ['korek','tali','batu'],
	'ransel' : ['timpani','pisau belati','kasur gulung','roti']
	}
>>> inventory20102186['saku'] = ['kerang','bandeng','berry','rumput laut']
>>> print(inventory20102186)
{'emas': 500, 'kantong': ['korek', 'tali', 'batu'], 'ransel': ['timpani', 'pisau belati', 'kasur gulung', 'roti'], 'saku': ['kerang', 'bandeng', 'berry', 'rumput laut']}
>>> inventory20102186['ransel'].sort()
>>> print(inventory20102186)
{'emas': 500, 'kantong': ['korek', 'tali', 'batu'], 'ransel': ['kasur gulung', 'pisau belati', 'roti', 'timpani'], 'saku': ['kerang', 'bandeng', 'berry', 'rumput laut']}
>>> inventory20102186['ransel'].remove('pisau belati')
>>> print(inventory20102186)
{'emas': 500, 'kantong': ['korek', 'tali', 'batu'], 'ransel': ['kasur gulung', 'roti', 'timpani'], 'saku': ['kerang', 'bandeng', 'berry', 'rumput laut']}
>>> inventory20102186.update({'emas' : 500+50})
>>> print(inventory20102186)
{'emas': 550, 'kantong': ['korek', 'tali', 'batu'], 'ransel': ['kasur gulung', 'roti', 'timpani'], 'saku': ['kerang', 'bandeng', 'berry', 'rumput laut']}
>>> 
>>> lst_nim = [20102186]
>>> def tambah20102186 (a,b,c,d):
	return a+b+c+d

>>> print(tambah20102186(10,20,0,0))
30
>>> print(tambah20102186(10,20,50,60))
140
>>> 
>>> lst_nim = [20102186]
>>> def tambah20102186(angka):
	hasil=0
	for a in angka:
		hasil=hasil+a
	return hasil

>>> tambah20102186([10,20])
30
>>> tambah20102186([10,20,50,60])
140
>>> 
>>> 
>>> Listku_2186 = [x for x in range(3,30) if x%2 == 0]
>>> print(Listku_2186)
[4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
>>> 
>>> bilangan2186 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
>>> a22186 = [bilangan2186[1], bilangan2186[3], bilangan2186[5], bilangan2186[7], bilangan2186[9]]
>>> b2186 = [bilangan2186[0], bilangan2186[3], bilangan2186[6], bilangan2186[9], bilangan2186[12]]
>>> print(a2186)
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    print(a2186)
NameError: name 'a2186' is not defined
>>> 
>>> bilangan2186 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
>>> a2186 = [bilangan2186[1], bilangan2186[3], bilangan2186[5], bilangan2186[7], bilangan2186[9]]
>>> b2186 = [bilangan2186[0], bilangan2186[3], bilangan2186[6], bilangan2186[9], bilangan2186[12]]
>>> print(a2186)
[1, 3, 5, 7, 9]
>>> print(b2186)
[0, 3, 6, 9, 12]
>>> 
>>> 
>>> bilangan2186 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
>>> ganjil2186 = []
>>> subtiga2186 = []
>>> for n in bilangan2186:
	if n%3==0:
		subtiga2186.append(n)

		
>>> for n in bilangan2186:
	if n%2 != 0 and  n != 11:
		ganjil2186.append(n)

		
>>> print(ganjil2186)
[1, 3, 5, 7, 9]
>>> print(subtiga2186)
[0, 3, 6, 9, 12]
>>> 
>>> kuadratkan_list_2186 = []
>>> kuadratkan_dict_2186 = {}
>>> for i in range (0,10):
	kuadratkan_list_2186.append(i*i)
	kuadratkan_dict_2186[i]=i*i

	
>>> print(kuadratkan_list_2186)
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> print(kuadratkan_dict_2186)
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
>>> 
>>> inventory2186 = {
	'emas' : 500,
	'kantong' : ['korek','tali','batu'],
	'ransel' : ['timpani','pisau belati','kasur gulung','roti']
	}
>>> inventory2186['saku'] = ['kerang','bandeng','berry','rumput laut']
>>> print(inventory2186)
{'emas': 500, 'kantong': ['korek', 'tali', 'batu'], 'ransel': ['timpani', 'pisau belati', 'kasur gulung', 'roti'], 'saku': ['kerang', 'bandeng', 'berry', 'rumput laut']}
>>> inventory2186['ransel'].sort()
>>> print(inventory2186)
{'emas': 500, 'kantong': ['korek', 'tali', 'batu'], 'ransel': ['kasur gulung', 'pisau belati', 'roti', 'timpani'], 'saku': ['kerang', 'bandeng', 'berry', 'rumput laut']}
>>> inventory2186['ransel'].remove('pisau belati')
>>> print(inventory2186)
{'emas': 500, 'kantong': ['korek', 'tali', 'batu'], 'ransel': ['kasur gulung', 'roti', 'timpani'], 'saku': ['kerang', 'bandeng', 'berry', 'rumput laut']}
>>> inventory2186.update({'emas' : 500+50})
>>> print(inventory2186)
{'emas': 550, 'kantong': ['korek', 'tali', 'batu'], 'ransel': ['kasur gulung', 'roti', 'timpani'], 'saku': ['kerang', 'bandeng', 'berry', 'rumput laut']}
>>> 
>>> def tambah2186 (a,b,c,d):
	return a+b+c+d

>>> print(tambah2186(10,20,0,0))
30
>>> print(tambah2186(10,20,50,60))
140
>>> 
>>> def tambah2186(angka):
	hasil=0
	for a in angka:
		hasil=hasil+a
	return hasil

>>> tambah2186([10,20])
30
>>> tambah2186([10,20,50,60])
140
>>> 
Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #List
>>> x2186 = [10, 20, 30]
>>> x2186
[10, 20, 30]
>>> type (x2186)
<class 'list'>
>>> x2186[0]
10
>>> x2186[1]
20
>>> x2186[2]
30
>>> for data2186 in x2186 :
	print (data2186)

	
10
20
30
>>> i2186 = 0
>>> while i2186 < 3 :
	print (x2186[i2186])
	i2186 += 1

10
20
30
>>> #negatif element
>>> y2186 = ['kucing', 'sapi', 'gajah', 'ikan']
>>> y2186[-1]
'ikan'
>>> y2186[-3]
'sapi'
>>> #sublist dengan slices
>>> y2186 = ['kucing', 'sapi', 'gajah', 'ikan']
>>> y2186[0:4]
['kucing', 'sapi', 'gajah', 'ikan']
>>> y[1:3]
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    y[1:3]
NameError: name 'y' is not defined
>>> y2186[1:3]
['sapi', 'gajah']
>>> y2186[0:-1]
['kucing', 'sapi', 'gajah']
>>> #menambahkan elemen list
>>> x2186 = [10, 20, 30]
>>> #menggunakan metode append()
>>> x2186.append(40)
>>> x2186
[10, 20, 30, 40]
>>> #menggunakan metode insert()
>>> x2186.insert(2, 50)
>>> x2186
[10, 20, 50, 30, 40]
>>> #menggunakan metode extend()
>>> x2186.extend([66, 77, 88])
>>> x2186
[10, 20, 50, 30, 40, 66, 77, 88]
>>> #menghapus elemen list
>>> x2186 = [10, 20, 30, 40, 50]
>>> #menggunakan perintah del
>>> del x2186[2]
>>> x2186
[10, 20, 40, 50]
>>> #menggunakan metode remove()
>>> x2186.remove(20)
>>> x2186
[10, 40, 50]
>>> #menggunakan metode pop()
>>> nilai = x2186.pop()
>>> nilai
50
>>> x2186
[10, 40]
>>> #mengurutkan elemen list
>>> x2186 = [50, 10, 40, 20, 30]
>>> #menggunakan fungsi sorted ()
>>> y2186 = sorted (x2186)
>>> y2186
[10, 20, 30, 40, 50]
>>> #menggunakan metode sort ()
>>> x2186.sort ()
>>> x2186
[10, 20, 30, 40, 50]
>>> #membalik urutan elemen list
>>> x2186 = [50, 10, 40, 20, 30]
>>> #menggunakan fungsi reverse()
>>> x2186.reverse ()
>>> x2186
[30, 20, 40, 10, 50]
>>> #selain menggunakan metode reverse(), kita dapat membuat fungsi sendiri
>>> def reverse (lst):
	temp2186 = []
	for element in lst [::-1]:
		temp2186.append (element)
	return temp2186

>>> #contoh penggunaan
>>> a2186 = [50, 10, 40, 20, 30]
>>> b2186 = reverse (a2186)
>>> b2186
[30, 20, 40, 10, 50]
>>> #mencari nilai minimal dan maksimal
>>> x2186 = [300, 210, 500, 100, 150]
>>> # menggunakan fungsi min()
>>> min(x2186)
100
>>> #menggunakan fungsi max()
>>> max(x2186)
500
>>> 
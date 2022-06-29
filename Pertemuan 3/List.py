Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = [10, 20, 30]
>>> x
[10, 20, 30]
>>> x[0]
10
>>> x[1]
20
>>> x[2]
30
>>> for data in x :
	print (data)

10
20
30
>>> i = 0
>>> while i < 3 :
	print (x[i])
	i += 1

10
20
30
>>> y = ['kucing', 'sapi', 'gajah', 'ikan']
>>> y[-1]
'ikan'
>>> y[-3]
'sapi'
>>> #sublist dengan slices
>>> y = ['kucing', 'sapi', 'gajah', 'ikan']
>>> y[0:4]
['kucing', 'sapi', 'gajah', 'ikan']
>>> y[1:3]
['sapi', 'gajah']
>>> y[0:-1]
['kucing', 'sapi', 'gajah']
>>> #menambahkan elemen list
>>> x = [10, 20, 30]
>>> #menggunakan metode append()
>>> x.append(40)
>>> x
[10, 20, 30, 40]
>>> #menggunakan metode insert()
>>> x.insert(2, 50)
>>> x
[10, 20, 50, 30, 40]
>>> #menggunakan metode extend()
>>> x.extend([66, 77, 88])
>>> x
[10, 20, 50, 30, 40, 66, 77, 88]
>>> #menghapus elemen list
>>> x = [10, 20, 30, 40, 50]
>>> #menggunakan perintah del
>>> del x[2]
>>> x
[10, 20, 40, 50]
>>> #menggunakan metode remove()
>>> x.remove(20)
>>> x
[10, 40, 50]
>>> #menggunakan metode pop()
>>> nilai = x.pop()
>>> nilai
50
>>> x
[10, 40]
>>> #mengurutkan elemen list
>>> x = [50, 10, 40, 20, 30]
>>> #menggunakan fungsi sorted ()
>>> y = sorted (x)
>>> y
[10, 20, 30, 40, 50]
>>> #menggunakan metode sort ()
>>> x.sort ()
>>> x
[10, 20, 30, 40, 50]
>>> #membalik urutan elemen list
>>> x = [50, 10, 40, 20, 30]
>>> #menggunakan fungsi reverse()
>>> x.reverse ()
>>> x
[30, 20, 40, 10, 50]
>>> #selain menggunakan metode reverse(), kita dapat membuat fungsi sendiri
>>> def reverse (lst):
	temp = []
	for element in lst [::-1]:
		temp.append (element)
	return temp

>>> #contoh penggunaan
>>> a = [50, 10, 40, 20, 30]
>>> b = reverse (a)
>>> b
[30, 20, 40, 10, 50]
>>> #mencari nilai minimal dan maksimal
>>> x = [300, 210, 500, 100, 150]
>>> # menggunakan fungsi min()
>>> min(x)
100
>>> #menggunakan fungsi max()
>>> max(x)
500
>>> 
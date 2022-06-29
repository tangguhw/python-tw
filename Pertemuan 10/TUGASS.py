Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Nomor 1
>>> max_20102186 = lambda m, n: m if m > n else n
>>> print(max_20102186(10,3))
10
>>> 
>>> #Nomor 2
>>> #a
>>> even_fn_20102186 = lambda x: True if x%2 == 0 else False
>>> print(even_fn_20102186(20))
True
>>> print(even_fn_20102186(11))
False
>>> 
>>> #Nomor 2
>>> #b
>>> prog_20102186 = lambda list: [x for x in list if x%2 == 0]
>>> print(prog_20102186([1,3,2,5,20,21]))
[2, 20]
>>> #fungsi list untuk membuat list dari objek iterable
>>> #fungsi lambda untuk mendeklarasikan lambda
>>> #x%2==0 untuk mencari bilangan genap
>>> 
>>> #Nomor 2
>>> #a
>>> even_fn_20102186 = lambda x: True if x%2 == 0 else False
>>> print(even_fn_20102186(20))
True
>>> print(even_fn_20102186(11))
False
>>> #even_fn_20102186 adalah nama yang digunakan pada fungsi diatas
>>> #fungsi lambda untuk mendeklarasikan lambda
>>> #x%2==0 untuk mencari bilangan genap
>>> 
>>> #Nomor 1
>>> max_20102186 = lambda m, n: m if m > n else n
>>> print(max_20102186(10,3))
10
>>> #max_20102186 adalah nama fungsi yang digunakan
>>> #fungsi lambda untuk mendeklarasikan lambda
>>> #m, n: m if m > n else n, kode tersebut untuk membandingkan dua buah nilai yang mana m = nilai maksimum dan n = nilai minimum
>>> 
>>> #Nomor 3
>>> Fahrenheit_List_20102186 = [98, 102, 110, 125]
>>> Fahrenheit_to_celcius_20102186 = map(lambda x: round(((5.00/9.00)*(x - 32)), 2), Fahrenheit_List_20102186)
>>> print(list(Fahrenheit_to_celcius_20102186))
[36.67, 38.89, 43.33, 51.67]
>>> #fungsi map() berfungsi untuk mengaplikasikan satu fungsi ke semua anggota dari iterable dan mengembalikan hasilnya berupa objek map
>>> #Nomor 4
>>> 
>>> 
>>> 
>>> #Nomor 4
>>> Tahun_List_20102186 = [1992, 1994, 1996, 1998, 2000, 2003, 2004, 2008, 2010, 2012, 2014]
>>> Tahun_Kabisat_20102186 = list(filter(lambda x: x % 4 == 0, Tahun_List_20102186))
>>> print(Tahun_Kabisat_20102186)
[1992, 1996, 2000, 2004, 2008, 2012]
>>> 
>>> 
>>> 
>>> #Nomor 5
>>> a = [5,9,2,4,7]
>>> b = [3,7,1,9,2]
>>> c = [6,8,0,5,3]
>>> max_20102186 = map(lambda x: max(x), zip(a,b,c))
>>> print(list(max_20102186))
[6, 9, 2, 9, 7]
>>> #max_20102186 digunakan untuk mencari nilai maksimal
>>> #fungsi list untuk membuat list dari objek iterable
>>> #fungsi map() berfungsi untuk mengaplikasikan satu fungsi ke semua anggota dari iterable dan mengembalikan hasilnya berupa objek map
>>> #fungsi zip() untuk membuat iterator berisi item dari buah iterable atau lebih dalam bantuan tuple
>>> 
>>> #Nomor 6
>>> my_list_20102186 = [12,65,54,39,102,339,221,50,70]
>>> prog_20102186 = [c for c in my_list_20102186 if c % 13 == 0]
>>> print(prog_20102186)
[65, 39, 221]
>>> #fungsi list() untuk membuat list dari objek iterable
>>> #fungsi digunakan() untuk menyaring anggota iterable dari sebuah fungsi untuk menguji tiap anggota pada iterable tersebut
>>> #x % 13 digunakan untuk menentukan bilangan yang dapat dibagi dengan 13
>>> 
>>> 
>>> #Nomor 7
>>> dict_a_20102186 = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]
>>> #a
>>> prog_20102186 = map(lambda x: x.get('name'), dict_a_20102186)
>>> print(list(prog_20102186))
['python', 'java']
>>> #b
>>> data_20102186 = map(lambda i: (i.get('points')*10), dict_a_20102186)
>>> print(list(data_20102186))
[100, 80]
>>> #fungsi list() untuk membuat list dari objek iterable
>>> #fungsi map() berfungsi untuk mengaplikasikan satu fungsi ke semua anggota dari iterable dan mengembalikan hasilnya berupa objek map
>>> #dict_a_20102186 = [{}] merupakan struktur data yang tidak berurutan
>>> 
>>> #Nomor 6
>>> my_list_20102186 = [12,65,54,39,102,339,221,50,70]
>>> prog_20102186 = [c for c in my_list_20102186 if c % 13 == 0]
>>> print(prog_20102186)
[65, 39, 221]
>>> #fungsi list() untuk membuat list dari objek iterable
>>> #fungsi digunakan() untuk menyaring anggota iterable dari sebuah fungsi untuk menguji tiap anggota pada iterable tersebut
>>> 
>>> #Nomor 6
>>> my_list_20102186 = [12,65,54,39,102,339,221,50,70]
>>> prog_20102186 = [c for c in my_list_20102186 if c % 13 == 0]
>>> print(prog_20102186)
[65, 39, 221]
>>> #fungsi list() untuk membuat list dari objek iterable
>>> #fungsi filter() digunakan untuk menyaring anggota iterable dari sebuah fungsi untuk menguji tiap anggota pada iterable tersebut
>>> #x % 13 digunakan untuk menentukan bilangan yang dapat dibagi dengan 13
>>> 
>>> #Nomor 4
>>> Tahun_List_20102186 = [1992, 1994, 1996, 1998, 2000, 2003, 2004, 2008, 2010, 2012, 2014]
>>> Tahun_Kabisat_20102186 = list(filter(lambda x: x % 4 == 0, Tahun_List_20102186))
>>> print(Tahun_Kabisat_20102186)
[1992, 1996, 2000, 2004, 2008, 2012]
>>> #fungsi list() untuk membuat list dari objek iterable
>>> #fungsi filter() digunakan untuk menyaring anggota iterable dari sebuah fungsi untuk menguji tiap anggota pada iterable tersebut
>>> #x: x % 4 == 0 untuk mencari tahun kabisat
>>> #lambda digunakan untuk mencari fungsi anonim
>>> 
>>> #Nomor 8
>>> list_a_20102186 = [1,2,3]
>>> list_b_20102186 = [10,20,30]
>>> prog_20102186 = map(lambda x: sum(x), zip(list_a_20102186, list_b_20102186))
>>> print(list(prog_20102186))
[11, 22, 33]
>>> #fungsi list() untuk membuat list dari objek iterable
>>> #fungsi map() berfungsi untuk mengaplikasikan satu fungsi ke semua anggota dari iterable dan mengembalikan hasilnya berupa objek map
>>> 
>>> #Nomor 9
>>> dict_a_20102186 = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]
>>> prog_20102186 = filter(lambda x: x['name']=='python', dict_a_20102186)
>>> print(list(prog_20102186))
[{'name': 'python', 'points': 10}]
>>> #fungsi list() untuk membuat list dari objek iterable
>>> #fungsi filter() digunakan untuk menyaring anggota iterable dari sebuah fungsi untuk menguji tiap anggota pada iterable tersebut
>>> #x: x['name']=='python', digunakan untuk menyeleksi name dan python
>>> 
>>> #Nomor 10
>>> death_20102186 = [
	('James','Dean',24),
	('Jimi','Hendrix',27),
	('George','Gershwin',38)]
>>> prog_20102186 = sorted(death_20102186, key=lambda x: x[0][2])
>>> print(prog_20102186)
[('James', 'Dean', 24), ('Jimi', 'Hendrix', 27), ('George', 'Gershwin', 38)]
>>> #fungsi sorted() untuk mengurutkan suatu iterable baik secara naik maupun turun
>>> #key merupakan kata kunci
>>> #x[0][2] untuk mengurutkan dari yang terkecil ke terbesar
>>> 
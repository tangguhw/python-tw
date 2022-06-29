Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #dictionary
>>> d2186 = {1:100, 2:200, 3:300, 4:400, 5:500}
>>> d2186
{1: 100, 2: 200, 3: 300, 4: 400, 5: 500}
>>> type (d2186)
<class 'dict'>
>>> d2186 = {1:100, 2:200, 3:300, 4:400, 5:500}
>>> d2186 [1]
100
>>> d2186 [2]
200
>>> d2186 [3]
300
>>> d2186 = {1:100, 2:200, 3:300, 4:400, 5:500}
>>> d2186.get(1)
100
>>> d2186.get(2)
200
>>> #indeks pada dictionary bisa berupa string
>>> d2186 = {'satu':100, 'dua':200, 'tiga':300}
>>> d2186 ['satu']
100
>>> d2186 ['dua']
200
>>> d2186 ['tiga']
300
>>> #elemen dictionary bisa berasal dari tipe apa saja
>>> pegawai2186 = {
	'nip' : "P001",
	'nama' : "Adi",
	'gaji' : 850000
	}
>>> pegawai2186 ['nip']
'P001'
>>> pegawai2186 ['nama']
'Adi'
>>> pegawai2186 ['gaji']
850000
>>> #menambahkan elemen dictionary
>>> #dictionary kosong
>>> d2186 = {}
>>> #menambahkan elemen
>>> d2186['satu']=100
>>> d2186['dua']=200
>>> d2186['tiga']=300
>>> d2186
{'satu': 100, 'dua': 200, 'tiga': 300}
>>> #mengubah elemen dictionary
>>> d2186 = {'satu': 100, 'dua': 200, 'tiga': 300}
>>> d2186
{'satu': 100, 'dua': 200, 'tiga': 300}
>>> #mengubah elemen
>>> d2186 ['dua'] = 900
>>> d2186
{'satu': 100, 'dua': 900, 'tiga': 300}
>>> #perintah dibawah ini akan menambahkan elemen baru
>>> #bukan mengubah elemen kedua
>>> d2186['Dua'] = 700
>>> d2186
{'satu': 100, 'dua': 900, 'tiga': 300, 'Dua': 700}
>>> len (d2186)
4
>>> #menghapus elemen dictionary
>>> d2186 = {'satu': 100, 'dua': 200, 'tiga': 300}
>>> #menghapus elemen pertama
>>> del d2186['satu']
>>> d2186 ['dua'] = 900
>>> d2186
{'dua': 900, 'tiga': 300}
>>> d2186 = {'satu': 100, 'dua': 200, 'tiga': 300, 'empat':400}
>>> d2186
{'satu': 100, 'dua': 200, 'tiga': 300, 'empat': 400}
>>> #daftar kunci yang akan dihapus
>>> keys2186 = ['satu', 'tiga']
>>> for key2186 in keys2186 :
	del d2186[key2186]

>>> d2186
{'dua': 200, 'empat': 400}
>>> 
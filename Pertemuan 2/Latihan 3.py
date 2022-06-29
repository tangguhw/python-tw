Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x2186 = int(input("Masukkan bilangan bulat : "))
Masukkan bilangan bulat : 10
>>> if x2186 > 0:
	print ("%d adalah bilangan bulat positif" %x2186)
elif x2186==0:
	print("%d adalah bilangan nol" %x2186)
else:
	print ("%d adalah bilangan negatif" %x2186)

	
10 adalah bilangan bulat positif
>>> print ("Masukkan data koordinat")
Masukkan data koordinat
>>> x2186 = int(input("Masukkan nilai x : "))
Masukkan nilai x : 2
>>> y2186 = int(input("Masukkan nilai y : "))
Masukkan nilai y : 3
>>> info = "koordinat (" + str(x2186) + ","  + str(y2186) +  ") berada pada kuadran"
>>> if (x2186 > 0 and y2186 <0):
    print (info + "I")
elif (x2186 < 0 and y2186 > 0):
    print (info + "II")
elif (x2186 < 0 and y2186 < 0) :
    print (info + "III")
elif (x2186  > 0 and y2186 < 0):
    print (info + "IV")
else:
    pass

>>> 

def cek_angka(bil_1, bil_2, bil_3):
    if (bil_1 == bil_2 == bil_3):
        print (False)
    elif (bil_1 + bil_2 == bil_3 or bil_2 + bil_3 == bil_1 or bil_1 + bil_3 == bil_2):
        print (True)
    else:
        print (False)
        
bil_1 = int(input("Masukan Bulangan pertama: "))
bil_2 = int(input("Masukan Bulangan kedua: "))
bil_3 = int(input("Masukan Bulangan ketiga: "))
cek_angka(bil_1,bil_2,bil_3)
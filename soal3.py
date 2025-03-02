try:
    bulan = int(input("Masukan bulan (1-12) bertipe integer: "))
    if bulan == 1 or bulan == 3 or bulan == 5 or bulan == 7 == bulan == 8 or bulan == 10 or bulan == 12:
        print("Jumlah Hari 31")
    elif bulan == 4 or bulan == 6 or bulan == 9 or bulan == 11:
        print("Jumlah Hari 30")
    elif bulan > 12:
        print("Jumlah bulan harus benar")
    else:
        print("Jumlah Hari 29")
except:
    print("Inputan bulan tidak valid")
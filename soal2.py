try:
    angka = int(input("Inputkan suatu bilangan: "))
    print("Positif" if angka %2 == 0 else "negatif" )
except:
    print("Input anda salah")
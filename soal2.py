bilangan_1 = int(input("Masukan Bulangan pertama: "))
bilangan_2 = int(input("Masukan Bulangan kedua: "))
bilangan_3 = int(input("Masukan Bulangan ketiga: "))

def cek_digit_belakang(bilangan_1, bilangan_2, bilangan_3):
    if bilangan_1 %10 == bilangan_2 %10 or bilangan_2 %10 == bilangan_3 %10 or bilangan_1 %10 == bilangan_3 %10:
        print("True")
    else:
        print("False")
    
cek_digit_belakang(bilangan_1, bilangan_2, bilangan_3)
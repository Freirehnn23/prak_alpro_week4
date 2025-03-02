try:
    sisi1 = int(input("masukan Sisi 1: "))
    sisi2 = int(input("masukan Sisi 2: "))
    sisi3 = int(input("masukan Sisi 3: "))

    if sisi1 == sisi2 and sisi2 == sisi3 and sisi1 == sisi3:
        print("3 sisi sama")
    elif sisi1 == sisi2 or sisi2 == sisi3 or sisi1 == sisi3:
        print("2 sisi sama")
    else:
        print("Tidak ada yang sama")
except:
    print("Input yang anda masukan salah, mohon imputkan integer")

def input_celcius(inputan_celcius= int(input("masukan suhu dalam celcius: "))):
    return inputan_celcius
def input_suhu(suhu_diinginkan= str(input("masukan suhu yang diinginkan(hanya dalam fahrenheit atau celcius): "))): 
    return suhu_diinginkan

dalam_fahrenheit = lambda input : (9/5) * input + 32
dalam_reamur = lambda input : 0.8 * input

def main():
    inputan = input_celcius()
    suhu_diinginkan = input_suhu()
    if suhu_diinginkan == "fahrenheit":
        hasil = dalam_fahrenheit(inputan)
        print("suhu dari celcius ke fahrenheit adalah: ", hasil)
    elif suhu_diinginkan == "reamur":
        hasil = dalam_reamur(inputan)
        print("suhu dari celcius ke reamur adalah: ", hasil)
    else:
        print("maaf suhu yang anda inginkan tidak tersedia dalam program ini")
        
main()

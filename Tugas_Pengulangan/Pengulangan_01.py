#File : pengulangan_01.py
# Program While-hitungsuhu
# Nama : Maliq Athaya Rinaldi
# Kamus Data
# x : var. input utk nilai data celcius (integer)
# y : var. input utk nilai data akhir (integer)
# z : var. input utk nilai data inkremen (integer)
# r : var. utk hitung reamur
# f : var. utk hitung fahrenheit
def main():
    x = int(input("awal = "))
    y = int(input("akhir = "))
    z = int(input("inkremen = "))
    print("C F R")
    while (x <= y):
       r = 4/5*x
       f = 9/5*x+32
       print(x,round(r,3),round(f,2))
       x = x + z

if __name__ == '__main__':
 main()
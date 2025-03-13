# File : analisis2.py 
# Penulis : Maliq Athaya Rinaldi
# Tujuan Program
# Program ini bertujuan untuk mengecek apakah suatu barang masih aman untuk dikonsumsi atau sudah kadaluarsa
# Kamus Data
# a = nama barang
# b = tanggal
# c = bulan
# d = tahun
# f = tanggal hari ini
# g = bulan hari ini
# h = tahun hari ini

a = input("Nama barang:")
b = int(input("Tanggal:"))
c = int(input("Bulan:"))
d = int(input("Tahun:"))

def main():
    print("="*25)
    print("Tanggal hari ini")
    f = int(input("Tanggal:"))
    g = int(input("Bulan:"))
    h = int(input("Tahun:"))
    print("="*25)


    if d < h:
        print(a,"sudah KADALUARSA, tidak boleh dimakan!")
    elif d > h:
        print(a,"masih aman dikonsumsi sampai dengan",b,"/",c,"/",d)
    else:

        if c < g:
            print(a,"sudah KADALUARSA, tidak boleh dimakan!")
        elif c > g:
            print(a,"masih aman dikonsumsi sampai dengan",b,"/",c,"/",d)
        else:
            if b < f:
                print(a,"sudah KADALUARSA, tidak boleh dimakan!")
            elif b >= f:
                print(a,"masih aman dikonsumsi sampai dengan",b,"/",c,"/",d)

if __name__ == "__main__":
    main()





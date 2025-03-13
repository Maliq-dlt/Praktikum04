#File : pengulangan_02.py
# Program While-JumlahData
# Nama : Maliq Athaya Rinaldi
# Kamus Data
# x : var. input utk nilai data x(integer)
# j : untuk menghitung berapa kali input data
# Jml : var. utk hitung jumlah data
def main():
    x = int(input(""))
    Jml = 0
    j = 0
    while (x != 9999):
        Jml = Jml + x
        j = j + 1
        x = int(input(""))
    print('Jumlah data ',round(Jml/j,2))

if __name__ == '__main__':
 main()
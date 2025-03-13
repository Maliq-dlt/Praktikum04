# Program Menghitung Rata-rata Data
# Kamus Data:
# x : nilai input data (integer)
# jumlah : menyimpan total nilai (integer/float)
# counter : menghitung jumlah data yang dimasukkan (integer)

def main():
    print("Masukkan nilai-nilai (9999 untuk mengakhiri):")
    x = int(input("Nilai: "))
    jumlah = 0
    counter = 0
    
    while x != 9999:
        jumlah += x
        counter += 1
        x = int(input("Nilai: "))
    
    if counter > 0:
        rata_rata = jumlah / counter
        # Menghilangkan .0 jika hasilnya bilangan bulat
        if rata_rata.is_integer():
            rata_rata = int(rata_rata)
            
        print(f"Jumlah data: {counter}")
        print(f"Total nilai: {int(jumlah)}")
        print(f"Rata-rata: {rata_rata}")
    else:
        print("Tidak ada data yang dimasukkan")

if __name__ == '__main__':
    main() 
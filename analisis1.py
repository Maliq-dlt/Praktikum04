# File : analisis1.py 
# Penulis : Maliq Athaya Rinaldi
# Tujuan Program
#untuk mengecek apakah nilai yang diinputkan berada di antara nilai yang lain
# Kamus Data
# a = nilai pertama
# b = nilai kedua
# c = nilai ketiga

def main():

     a = int(input("a:"))
     b= int(input("b:"))
     c = int(input("c:"))

     if a > b and b > c:
        print("nilai", b,"di antara",c,"dan",a)
     elif b > a and a > c:
        print("nilai", a,"di antara",c,"dan",b)
     elif a > c and c > b:
        print("nilai", c,"di antara",b,"dan",a)
     elif b > c and c > a:
        print("nilai", c,"di antara",a,"dan",b)
     elif c > a and a > b:
        print("nilai", a,"di antara",b,"dan",c)
     elif c > b and b > a:
        print("nilai", b,"di antara",a,"dan",c)

if __name__ == "__main__":
    main()
        

#File : kuis_3.py
#Program pembagian OSN
#Kamus data
#n = input nama
#k = input Kelas (10,11,12)
#m = input nilai Matematika (0..100)
#f = input nilai Fisika (0..100) 
#k_i = input nilai Kimia (0..100) 
#b = input nilaiBiologi (0..100)
#b_i =input nilai Bahasa Inggris (0..100)
#b_w = input untuk apakah Buta Warna (yes/no)
#k_r = input apakah bisa memggunakan Komputer (yes/no) 
#o = input berapa kali OSN (0..2) 
def main():
    n = input("Nama :")
    k = int(input("Kelas (10,11,12) :"))
    m = int(input("Matematika (0..100) :"))
    f = int(input("Fisika (0..100) :"))
    k_i = int(input("Kimia (0..100) :"))
    b = int(input("Biologi (0..100) :" ))
    b_i =int(input("Bahasa Inggris (0..100) :"))
    b_w = input("Buta Warna (yes/no) :")
    k_r = input("Komputer (yes/no) :")
    o = int(input("OSN (0..2) :"))
    
    if (k==11) or (k==10):
        print("OSN yang dapat diikuti",n," :")
        if (m>=80 and m<=100):
            print("Matematika")
        if (f>=80 and f<=100):
            print("Fisika")
        if b_w == "yes":
            print("tidak ada")
        elif (m<80 and f<80 and k_i<80 and b<80 and b_i<80):
            print("tidak ada")
        else:
            if (k_i>=80 and k_i<=100):
                print("Kimia")
        if (b>=80 and b<=100) and (m>=80 and m<=100) and (k_i>=80 and k_i<=100) and (b_i>=80 and b_i<=100):
            print("Biologi")
        if (k_r=="yes") and (m>=80 and m<=100) and (b_i>=80 and b_i<=100):
            print("Informatika")
        
    else:
        if (o>=2):
            print(n,"tidak dapat mengikuti OSN karena :")
            print("Kelas",k)
            print("OSN sudah",o,"kali")   
        elif (k>11) or (k<10):
            print(n,"tidak dapat mengikuti OSN karena :")
            print("Kelas",k)   

if __name__== '__main__':
    main()
            
            


#File : kuis_3.py
#Program menghitung skor prestasi dan sertifikat
#Kamus data
#s = Untuk kode sertifikat
#b = banyak sertifikat
#p = untuk kode prestasi
#b_2 = banyak prestasi
#t_s = untuk menyimpan skor sertifikat
#t_p =  untuk menyimpan skor prestasi
def main():
    
    s = input("kode sertifikat :")
    b =int(input("Banyak :"))
    p =input("kode prestasi :")
    b_2 = int(input("Banyak :"))
    t_s =0
    t_p =0
    
    if (s=="s1"):
        t_s+=b*100
    elif (s=="s2"):
        t_s+=b*50
    elif (s=="s3"):
        t_s+=b*30
    if (p=="p1"):
        t_p+=b_2*300
    elif(p=="p2"):
        t_p+=b_2*100
    print("Total nilai sertifikat :",t_s)
    print("Total nilai prestasi :",t_p)
    print("Total nilai :",t_s+t_p)
    
    
if __name__=='__main__':
    main()
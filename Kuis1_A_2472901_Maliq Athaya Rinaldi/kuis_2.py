#File : kuis_2.py
#Program membagi tinggi ke dalam dm dan inchi
#Kamus data
#n = untuk menginput nama
#t = untuk menginput tinggi
def main ():
    n =input("Nama :")
    t = int(input("tinggi :"))
    
    print ("Tinggi badan", n , round(t/100,2),"meter","atau",t//10,"dm","atau",round(t/2.54,2),"inci")
    
if __name__== '__main__':
    main()
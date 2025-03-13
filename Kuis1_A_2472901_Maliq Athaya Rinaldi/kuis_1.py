#File : kuis_1.py
#Program membagi tinggi ke dalam dm dan inchi
#Kamus data
#a = nilai a
#b = nilai b
def main ():
    a=int(input("nilai a :"))
    b=int(input("nilai b :"))
    
    if (a%b<=5) :
        if (a>10) and (b<5) :
            a = a+b
    else :
        b = b-a
        if (b%a>=0):
            c=b/a
    print("nilai hasil",a,b,c)
if __name__=='__main__':
    main()
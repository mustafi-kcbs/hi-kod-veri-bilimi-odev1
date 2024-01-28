 #1
x=3
x=float(x)

y=4.5
y=int(y)

z="8"
z=int(z)

a="12"
a=float(a)

b="46.8"
b=int(b)

print(x)
print(y)
print(z)
print(a)
print(b)

 #2
ahmet=20
mehmet=27
ela=24

print(ahmet==mehmet)
print(ela!=mehmet)
print(ela>ahmet)
print(ela<=mehmet)
print(ahmet>ela or ahmet<mehmet)
print(ahmet>ela and ahmet<mehmet)
print(not(ahmet>ela and ahmet<mehmet))


#3
x=int(input("Lutfen bir sayi giriniz:"))
y=int(input("Lutfen bir sayi giriniz:"))
z=x+y
t=x-y
k=x*y
l=x/y
liste=[]
print("liste","=",z,t,k,l)


#4
isim=input("Lutfen isminizi giriniz:")
yas=input("Lutfen yasinizi giriniz:")
sehir=input("Lutfen yasadiginiz sehri belirtiniz:")
meslek=input("Lutfen mesleginizi belirtiniz:")
print(isim, yas, sehir, meslek)

#5
"Hi-Kod Veri Bilimi Atolyesi"
print("Hi-Kod")
print("Veri")
print("Bilimi")
print("Atolyesi")
print("Veri"+"Bilimi")
print("Hi"+"Kod")

cumle="Hi-Kod Veri Bilimi Atolyesi"
cumle=cumle.upper()
print(cumle)

cumle="Hi-Kod Veri Bilimi Atolyesi"
cumle=cumle.lower()
print(cumle)


sayi=0,1,2,3,4,5,6,7,8,9
cift_sayi=sayi[0:9:2]
tek_sayi=sayi[1:9:2]
print(cift_sayi)
print(tek_sayi

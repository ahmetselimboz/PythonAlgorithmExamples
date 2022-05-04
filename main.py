"""
1) Ekranda "Merhaba Dünya" yazdıran kod örneği
"""
print("Merhaba Dünya")

"""
2) Kullanıcının ismini alarak merhaba (Kullanıcı İsmi) yazdıran kod örneği
"""
isim = input("İsminizi giriniz: ")
print("Merhaba " + isim)

"""
3) Girilen iki sayıyı toplayan kod örneği 
"""
sayi1 = float(input("Birinci sayiyi giriniz: "))
sayi2 = float(input("İkinci sayiyi giriniz: "))
print("Toplam: " + str(sayi1+sayi2))

"""
4) Girilen iki sayının ortalamasını bulan kod örneği
"""
sayi3 = float(input("Birinci sayiyi giriniz: "))
sayi4 = float(input("İkinci sayiyi giriniz: "))
print("Toplam: " + str((sayi3+sayi4)/2))

"""
5) Girilen vize ve final notunun ortalamasını hesaplayan kod örneği
"""
vize = float(input("Vize notunuzu giriniz: "))
final = float(input("Final notunuzu giriniz: "))
print("Toplam: " + str(vize*(40/100)+(final*(60/100))))

"""
6) Yazılı ortalaması girilen öğrencinin sınıf geçme durumunu gösteren kod örneği
"""
vize = float(input("Vize notunuzu giriniz: "))
final = float(input("Final notunuzu giriniz: "))
ortalama = (vize*(40/100)+(final*(60/100)))

if ortalama >= 50:
    print(f"Ortalamanız: {ortalama} geçtiniz")
else:
    print("Kaldınız")
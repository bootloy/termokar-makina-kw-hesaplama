
print("   ______   ______   ____     __  ___   ____     __ __    ___       ____ ")
print("  /_  __/  / ____/  / __ \   /  |/  /  / __ \   / //_/   /   |     / __ \ ")
print("   / /    / __/    / /_/ /  / /|_/ /  / / / /  / ,<     / /| |    / /_/ / ")
print("  / /    / /___   / _, _/  / /  / /  / /_/ /  / /| |   / ___ |   / _, _/ ")
print(" /_/    /_____/  /_/ |_|  /_/  /_/   \____/  /_/ |_|  /_/  |_|  /_/ |_| ")







print("-Termokar Makina (KW) Hesaplama-")


def Carp(x, y):
    return x * y


def Bol(x, y):
    return x / y


def Topla(x, y, z):
    return x + y + z

def Cikar(x, y):
    return x - y


secim = input("Başlatmak için 'Enter'a Bas:")




sayac = 0
sayi0 = 0
sayi = 0.746

sayi1 = float(input("Kompresör HP (Toplam): "))
sayi2 = float(input("Su Pompası HP (Toplam): "))
sayi3 = float(input("Fan Adeti Giriniz : "))

fan500 = 0.710
fan630T = 0.900
fan630P = 1.4
fan800 = 1.7

kompwat = Carp(sayi1, sayi)
supompwat = Carp(sayi2, sayi)
fanwat500 = Carp(sayi3, fan500)
fanwat630T = Carp(sayi3, fan630T)
fanwat630P = Carp(sayi3, fan630P)
fanwat800 = Carp(sayi3, fan800)
sonuca = Topla(kompwat, supompwat, fanwat500)
sonucb = Topla(kompwat, supompwat, fanwat630T)
sonucc = Topla(kompwat, supompwat, fanwat630P)
sonucd = Topla(kompwat, supompwat, fanwat800)

print("------------FAN ÇAPINA GİRİNİZ------------")
print("a- 500")
print("b- 630T")
print("c- 630P")
print("d- 800")
print(" Lütfen işlem yapmak için a-b-c-d seçeneklerinden birini seçiniz. ")

aa = bb = cc = dd = input("Harf Giriniz :")


if aa == 'a':

    print(sonuca)
    print(" (KW) ")

if bb == 'b':

    print(sonucb)
    print(" (KW) ")

if cc == 'c':

    print(sonucc)
    print(" (KW) ")

if dd == 'd':

    print(sonucd)
    print(" (KW) ")
print(" -------------TOPLAM ÇEKİLEN GÜÇ (KW)------------- ")

print(" ************ HASAN AYDIN BY PRODUCED ************ ")

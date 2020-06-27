print("Feladat1: Euroátváltó")
bekerForint=input("Kérem adja meg hány forintot szeretne beváltani:")
Forint=int(bekerForint)
euroArfolyam=315
#euroKifizet=0
euroKifizet=Forint//euroArfolyam
print("Önnk ennyi eurót ér a forintja: ")
print(euroKifizet)
#----------------------------------------------------- #
print("Feladat2:Éves fizetés")
haviber=input("Kém adjameg a havi fizetését és megmonom mennyi az éve fizetése:")
havipenz=float(haviber)
evesber=havipenz*12
print(evesber)
#-----------------------------------------------------#
print("Feladat3:Teglalap kerülete, területe")
Aoldal=input("Kérem adja meg az a oldalt: ")
a=float(Aoldal)
Boldal=input("Kérem adja meg a b oldalt: ")
b=float(Boldal)
Kerulet=2*(a+b)
print("A téglalap kerülete:")
print(Kerulet)
Terulet=a*b
print("A téglalap területe:")
print(Terulet)
#-----------------------------------------------------#
print("Feladat4: kör kerülete területe")
SugarBeker=input("kérem adja meg a kör kerületét: ")
sugar=float(SugarBeker)
import math
KorKerulet=2*sugar*(math.pi)
print("kör kerülete:")
print(KorKerulet)
KorTerulet=(sugar**2)*(math.pi)
print("A kör területe: ")
print(KorTerulet)
#---------------------------------------------------#
print("Feladat5: pithagorasz tétel")
Abeker=input("Kérem adja meg az egyik befogót: ")
befogo1=float(Abeker)
Bbeker=input("Kérem adja meg a  másik befogót: ")
befogo2=float(Bbeker)
import math
atfogo=math.sqrt((befogo1**2)+(befogo2**2))
print("Az átfogó hossza: ")
print(atfogo)
#----------------------------------------------------#
print("Feladat6: Átlag sebesség")
utBeker=input("Kérem adja meg az út hosszát: ")
Ut=float(utBeker)
idoBeker=input("Kérem adja meg az utazási idő hosszát: ")
Ido=float(idoBeker)
Sebesseg=Ut/Ido
print("Az ön átlag sebessége: ")
print(Sebesseg)
#------------------------------------------------------#
print("Feladat7: üzemanyag")
fogyasztasBeker=input("Kérem adja meg 100km-en mekkora az autó fogyasztása: ")
Fogyasztas100=float(fogyasztasBeker)
Fogyasztas1km=Fogyasztas100/100
utBeker=input("Kérem adja meg az út hosszát: ")
Ut=float(utBeker)
arBeker=input("Kérem adja meg 1 liter benzin ára: ")
BenzinAr=float(arBeker)
Utikoltseg=Ut*Fogyasztas1km*BenzinAr
print("Az ön autója ezen az úton ennyi költséget fog jelenteni")
print(Utikoltseg)
#--------------------------------------------------#
print("Feladat8: testömegindex")
testomegBe=input("Kérem adja meg a testsúlyát kg-ben: ")
Tomeg=float(testomegBe)
magassagBe=input("Kérem adja meg a magasságát cm-ben: ")
MagassagMeter=float(magassagBe)/100
Testomegindex=(Tomeg/(MagassagMeter**2))
print("Az ön testömegindexe:")
print(Testomegindex)
if 0<Testomegindex and Testomegindex<16:
    print("súlyosan sovány")
elif 16<=Testomegindex and Testomegindex<17:
    print("mérsékelt soványság")
elif 17<=Testomegindex and Testomegindex<18.5:
    print("enyhén soványság")
elif 18.5<=Testomegindex and Testomegindex<25:
    print("normál testsúly")
elif 25<=Testomegindex and Testomegindex<30:
    print("túlsúlyos")
elif 30<=Testomegindex and Testomegindex<35:
    print("I. fokú elhízott")
elif 35<=Testomegindex and Testomegindex<40:
    print("II.fokú elhízás")
elif 40<=Testomegindex:
    print("súlyos elhízás")
#-----------------------------------------------------#
print("Feladat9: Bankautonata")
penzBe=input("Mekkora összeget szeretne felvenni: ")
Penz=float(penzBe)
if Penz%1000==0:
    print("Felvehető összeg")
    Tizezresek=Penz//10000
    print("Tízezresek száma: ")
    print(Tizezresek)
    MaradekTizezresbol=Penz%10000
    Otezres=MaradekTizezresbol//5000
    print("ötezresek száma: ")
    print(Otezres)
    MaradekOtezresek=MaradekTizezresbol%5000
    Ketezres=MaradekOtezresek//2000
    print("kétezresek száma: ")
    print(Ketezres)
    MaradekKetezresek=MaradekOtezresek%2000
    Ezres=MaradekKetezresek//1000
    print("ezresek száma")
    print(Ezres)
else:
    print("Nem felvehető összeg")
#-------------------------------------------------------#
print("Felada10: Dolgozat pontszám osztályzás")
pontokBe=input("Kérem adja meg a pontszámát: ")
Pont=float(pontokBe)
if 0<Pont and Pont<101:
    print("Kiértékelem")
    if 0<=Pont and Pont<43:
        print("eredmény: elégtelen")
    elif 43<=Pont and Pont<57:
        print("eredménye: elégséges")
    elif 58<=Pont and Pont<72:
        print("eredménye: közepes")
    elif 73<=Pont and Pont<87:
        print("eredménye: jó")
    elif 88<=Pont and Pont<=100:
        print("eredménye: jeles")
else:
    print("Nem tudom kiértékelni, indíts újra")
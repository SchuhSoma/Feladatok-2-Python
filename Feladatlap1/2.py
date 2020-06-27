#---------------------------------------------------------------------------#
print("Feladat1: Random szám generálás")
import random
RandomSzam=random.randrange(1,15)
print("Az ön által generált szám: ", RandomSzam)
#------------------------------------------------------------------------------#
print("Feladat2: Generáljon 0 és 25 között egy tizedestört és egy egész számot")
import random
Egesz=random.randrange(0,25)
print("A generált egész szám: ",Egesz)
Tizedes=random.randrange(0,2500)/100
print("A generált tizedestört: ",Tizedes)
#------------------------------------------------------------------------------#
print("Feladat3: 6 kocka dobás szimulálása")
import random
Kocka=0
for i in range(6):
    Kocka=random.randrange(1,6)
    print(i+1," dobás: ",Kocka)
#------------------------------------------------------------------------------#
print("Feladat4: Összeg és átlag számítás")
import random
Kocka2=0
Osszeg=0
Atlag=0
for i in range(5):
    Kocka2=random.randrange(10,20)
    print(i+1," dobás: ",Kocka2)
    Osszeg+=Kocka2
Atlag=Osszeg/5
print("Az öt dobás összege: ",Osszeg)
print("A dobások átlaga: ",Atlag)
#------------------------------------------------------------------------------#
print("Feladat5: Szamjaték, kitalálod a számot")
import random
GepiSzam=random.randrange(0,100)
felhasznaloBe=input("Kérem adja meg a számot amire gondol: ")
FelhasznaloSzam=int(felhasznaloBe)
if(GepiSzam==FelhasznaloSzam):
    print("\tGratulálok te nyertél")
    print("A gép által generált szám: ",GepiSzam)
else:
    print("\tSajnálom most nem nyertél")
    print("A gép által generált szám: ", GepiSzam)

#------------------------------------------------------------------------------#
print("Fealadat6: összeadós játék")
import random
jo=0
rossz=0
for i in range(5):
    Aszam=random.randrange(0,100)
    Bszam=random.randrange(0,100)
    Cszam=Aszam+Bszam
    print("Találja ki mennyi a két szám eredménye:\n\t",Aszam, "+", Bszam, "=")
    felhasznaloBe=input("Kérem adja meg az eredményt: ")
    FelhasznaloSzam=int(felhasznaloBe)
    if(Cszam==FelhasznaloSzam):
        jo+=1
        print("\tGratulálok eltalálta")
        print("\tA két szám összege: ",Cszam)
    else:
        rossz+=1
        print("\tSajnálom az eredményt nem találta el\nA két szám összege: ",Cszam)
if(jo>rossz):
    print("\n\tJó vagy matekból")
else:
    print("\n\tGyakorolnod kell még")
#Ülesanne 1
num1 = int(input("Sisesta esimene täisarv: "))
num2 = int(input("Sisesta teine täisarv: "))

summa = num1 + num2
vahe = num1 - num2
korrutis = num1 * num2

print("Summa: ", summa)
print("Vahe: ", vahe)
print("Korrutis: ", korrutis)

#Ülesanne 2
KAESOLEV_AASTA = 2025

nimi = input("Sisesta oma nimi: ")
vanus = int(input("Sisesta oma vanus: "))

print("Tere, ", nimi + "!")
sunniaasta = KAESOLEV_AASTA - vanus
print("Sinu sunniaasta on ilmselt " , sunniaasta)

#Ülesanne 3
a = int(input("Sisesta esimene arv: "))
b = int(input("Sisesta teine arv: "))

print("Enne vahetamist: a =", a, ", b =", b)
print("Peale vahetamist: a =", b, ", b =", a)

#Ülesanne 4
sekundid = int(input("Sisesta sekundid: "))

if sekundid < 0:
    print("Vigane sisend!")
else:
    tunnid = sekundid // 3600
    minutid = (sekundid % 3600) // 60
    sekundid = sekundid % 60
    
print("Tegemist on ajaga: %02d:%02d:%02d" % (tunnid, minutid, sekundid))
    
#Ülesanne 5
LENNUFIRMA = "NATIONAL AIRLINE"
LAIUS = 40

LEND_AEG_MINUTIES = 105

lennunr = input("Sisesta lennunumber: ")
valjumine = input("Sisesta väljumislennujaama kood: ")
sihkoht = input("Sisesta sihtlennujaama kood: ")
valjumisaeg = input("Sisesta väljumise aeg (TT:MM): ")














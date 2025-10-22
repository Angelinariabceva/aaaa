#A5
tekst = ""

while True:
    print("\nMenüü:")
    print("1. Sisesta tekst")
    print("2. Kärbi servad (strip)")
    print("3. Eemalda topeltvahed kuni ühekordseks")
    print("4. Näita pikkust ilma tühikuteta")
    print("5. Välju")
    
    valik = input("Vali tegevus (1-5): ")
    
    if valik == "1":
        tekst = input("Sisesta tekst: ")
        
    elif valik == "2":
        if tekst == "":
            print("Sisesta tekst kõigepealt")
        else:
            tekst = tekst.strip()
            print("Pärast kärpimist:", tekst)
            
    elif valik == "3":
        if tekst == "":
            print("Sisesta tekst kõigepealt")
        else:
            # Eemalda topeltvahed ainult while abil
            while "  " in tekst:
                tekst = tekst.replace("  ", " ")
            print("Pärast topeltvahede eemaldust:", tekst)
            
    elif valik == "4":
        if tekst == "":
            print("Sisesta tekst kõigepealt")
        else:
            pikkus = len(tekst.replace(" ", ""))
            print("Pikkus ilma tühikuteta:", pikkus)
            
    elif valik == "5":
        print("Väljun programmist.")
        break
        
    else:
        print("Vale valik, palun proovi uuesti.")
        
 
 #B
def kontrolli_kasutajanimi():
    while True:
        kasutajanimi = input("Sisesta kasutajanimi: ")

        if kasutajanimi != kasutajanimi.strip():
            print("Viga: kasutajanime alguses või lõpus ei tohi olla tühikuid.")
            continue

        if ' ' in kasutajanimi:
            print("Viga: kasutajanimes ei tohi olla tühikuid.")
            continue

        if len(kasutajanimi) < 4:
            print("Viga: kasutajanimi on liiga lühike. Vähemalt 4 tähemärki.")
            continue
        if len(kasutajanimi) > 12:
            print("Viga: kasutajanimi on liiga pikk. Maksimaalselt 12 tähemärki.")
            continue

        if not kasutajanimi.isalnum():
            print("Viga: kasutajanimi tohib sisaldada ainult tähti ja numbreid.")
            continue

        print(f"Kasutajanimi '{kasutajanimi}' sobib!")
        break

kontrolli_kasutajanimi()

#C
def puhasta_ja_jaga(prompt="Sisesta F/N (või F/N/P): "):
    while True:
        sisend = input(prompt)
 
        sisend = sisend.strip()

        sisend = ' '.join(sisend.split())
   
        osad = sisend.split(' ')

        if len(osad) < 2:
            print("Palun sisesta vähemalt kaks osa (nt F N või F N P). Proovi uuesti.")
            continue
        
        osad = [osa.title() for osa in osad]
        return osad

tulemus = puhasta_ja_jaga()
print("Töödeldud osad:", tulemus)


#A
def puhasta_tekst(sisend):
    sisend = sisend.strip() 
    puhastatud = ""
    prev_space = False 

    for märk in sisend:
 
        if märk == '\t' or märk == '\n':
            märk = ' '

        if märk.isalpha() or märk.isdigit() or märk == ' ':
            if märk == ' ':
                if not prev_space:
                    puhastatud += märk
                    prev_space = True
            else:
                puhastatud += märk
                prev_space = False
       

    return puhastatud.strip()  

tekst = """Tere,  see on   näidis tekst.\nSiin on mitmed   tühikud,\tka tabid ja reavahetused."""

print("Algne tekst:")
print(tekst)
print("\nPuhastatud tekst:")
print(puhasta_tekst(tekst))


#B
kokku_ridu = 0
tuhjad_ridu = 0
luhikesed_ridu = 0

print("Sisesta ridu (sisesta tühi rida lõpetamiseks):")

while True:
    rida = input()
    if rida == "":
        break

    kokku_ridu += 1
    puhastatud = rida.strip()

    if puhastatud == "":
        tuhjad_ridu += 1
    elif len(puhastatud) < 5:
        luhikesed_ridu += 1

print(f"Kokku ridu: {kokku_ridu}")
print(f"Tühje ridu: {tuhjad_ridu}")
print(f"Lühikesi ridu (<5 tähemärki): {luhikesed_ridu}")


#C
sisend = input("Sisesta nimed komadega eraldatult: ").strip()

indeks = 0
nimi = ""

while indeks < len(sisend):
    märk = sisend[indeks]
    if märk != ',':
        nimi += märk
    else:
        puhastatud_nimi = nimi.strip()
        if puhastatud_nimi:
            print(f"Hello, {puhastatud_nimi.title()}!")
        nimi = ""  
    indeks += 1

puhastatud_nimi = nimi.strip()
if puhastatud_nimi:
    print(f"Hello, {puhastatud_nimi.title()}!")

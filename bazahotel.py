import bs4
import requests
import random

def tabelaHotel():
    #cardHeading - hoteli
    listaHotela = []
    listaHotelaFinal = []
    karakteri = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNMčČćĆšŠđĐžŽ- .,0123456789"
    #Skidamo podatke sa url-a
    url = "https://kopaonik.travel/hoteli/"
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text , "lxml")

    #filtriramo podatke kako bi izbegli nepotrebne karaktere i cuvamo u listu
    for i in soup.select(".cardHeading"):
        podatak = i.text
        listaHotela.append(str(podatak))
    for j in listaHotela:
        listaHotelaFinal.append(''.join(c for c in j if c in karakteri))

    #Kreiramo random kategorije
    listaKategorija = []
    for i in range(len(listaHotelaFinal)):
        broj = random.randint(1,6)
        if(broj == 1):
            podatak = str(broj) + " zvezdica"
        else:
            podatak = str(broj) + " zvezdice"
        listaKategorija.append(podatak)

    #Popunjavamo tabelu hotel u nasoj bazi
    for i in range(len(listaKategorija)):
        print("INSERT INTO hotel (naziv,kategorija) VALUES (" +listaHotelaFinal[i]+","+listaKategorija[i]+");")


def tabelaVrstaSobe():
    #Hotel ima 3 vrste soba(Standard,Porodicni,Apartman)
    opisi = ["Standard: Opremu hotelske sobe čine: krevet, noćni ormaric "+
"ili polica uz svako mesto za spavanje, ormar ili ugradna garderoba,"+
"radni sto ili stocic, ogledalo, zidna vecalica za garderobu i noćna lampa."+
"Pored toga, u prostoriji se može nalaziti i takva oprema kao što su televizor,"+
"telefon, radio, itd... U osnovnu opremljenost spada i kupatilo – može biti različito opremljeno,"+
"zavisi od standarda hotela, gde možete očekivati ​​dodatke kao što su peškiri za kupanje, set sapuna"+
"za svaku osobu, te u hotelima viših standarda fenove za kosu, vage i drugi kozmetički pribor." ,

"Porodični: Porodične sobe su obično proširena verzija standardne sobe. Takve sobe imaju veći prostor."+
"Opremljenost se ne razlikuje značajno od gore opisane - može se prilagoditi za smeštaj većeg broja gostiju."+
"(na primer veći ormar, više stolica, prostranije kupatilo).",

"Apartmani: Apartmani (skraćenica: APT) su sobe sa standardnom opremom, dodatno opremljene čajnom kuhinjom,"+
"posuđem i priborom za jelo. U ovim sobama možete pripremati obroke za sebe. U nekim slučajevima"+
"mogu se sastojati čak i od 2 odvojene prostorije (na primjer za decu)."
]


#biramo jednu sobu iz liste opisi
#i jedan nasumicni broj koji predstavlja cenu na dan
    for i in range(0,3):
        print("INSERT INTO vrsta_sobe(opis,cenaDan) VALUES ("+str(opisi[i])+","+str(random.randint(100,230)))
        


def tabelaSoba():
    #random biramo dodatni opis sobe
    dodatniOpisSobe = ["Soba je sa pogledom na planinu, poseduje bazen u dvoristu, garazu za automobil i djakuzi",
                   "Soba je sa pogledom na setaliste, velikom terasom i opremljenom kuhinjom",
                   "Soba je sa pogledom na dvoriste, tokom boravka u ovoj sobi ce biti promenjena posteljina na 5 dana",
                   "Soba poseduje Sony playstation 4, koji gosti mogu da igraju potpuno besplatno, dostupne igrice su (PES-20, FIFA 19 , Call of Duty, GTA V)",
                   "U ovoj sobi je dozvoljen pristup kucnim ljubimcima"
                   ]
    #nasumicno kreiramo ID za hotel i vrstu (id hotela i vrste moraju da postoje, nije moguce imati id hotela 10, ako imam samo 9 hotela u bazi)
    for i in range(1,30):
        id_hotela = random.randint(1,10)
        id_vrste = random.randint(1,3)
        opis = random.choice(dodatniOpisSobe)
        #upit za popunjavanje tabele sobe
        print("INSERT INTO soba(opis,hotel_id,vrsta_id) VALUES ("+ str(opis)+","+str(id_hotela)+","+str(id_vrste)+")")



def tabelaGost():
    imena = ["Danilo", "Tina" , "Sasa" , "Ljiljana","Nena", "Petar", "Djordje", "Uros", "Igor", "Goran", "Zoran","Snezana"]
    prezimena = ["Markovic" , "Nikolic" , "Stefanovic" , "Gajic" , "Lazic", "Mitrovic" , "Jovic", "Ilic", "Jovicic", "Prlic"]
    
    for i in range(1,30):
        JMBG = random.randint(100000000000000, 999999999999999)
        ime = random.choice(imena)
        prezime = random.choice(prezimena)
        print("INSERT INTO gost(ime,prezime,JMBG) VALUES ("+str(ime)+","+str(prezime)+","+str(JMBG)+");")


def tabelaStrani():
    drzave = ["Srbija", "Crna Gora", "Bosna i Hercegovina", "Hrvatska", "Makedonija", "Rumunija", "Madjarska"]

    for i in range(1,30,2):
        if(i>0):
            print(i)
            drzava = random.choice(drzave)
            pasos = random.randint(111111,999999)
            idGosta = i
            print("INSERT INTO strani(drzava,br_pasosa,id_gost) VALUES ("+str(drzava)+","+str(pasos)+","+str(idGosta)+");")


def tabelaDomaci():
    gradovi = ["Beograd" , "Jagodina" , "Arandjelovac" , "Kragujevac" , "Nis" , "Valjevo" , "Paracin" , "Novi Sad"]
    adrese = ["Branka Radicevica 8" , "Stevana Jakovljevica bb" , "Nikole Tesle 14" , "Omladinskih brigada 15" , "Kneza Lazara 22"]    
    for i in range (1,30,2):
        idGosta = str(i)
        grad = random.choice(gradovi)
        adresa = random.choice(adrese)

        print("INSERT INTO domaci(grad,adresa,id_gost) VALUES ("+str(grad)+","+str(adresa)+","+str(idGosta)+");")
        



def tabelaIznajmljuje():
    brojac = 29
    for i in range(1,30,2):
        
        print(i)
        godina1 = 2020
        mesec1 = random.randint(1,9)
        provera = mesec1
        if mesec1<10:
            mesec1 = "0"+str(mesec1)  
        dan1 = random.randint(1,32)
        if dan1<10:
            dan1 = "0"+str(dan1)
        sati1 = random.randint(1,25)
        if sati1<10:
            sati1 = "0"+str(sati1)  
        minuti1 = random.randint(0,60)
        if minuti1<10:
            minuti1 = "0"+str(minuti1)
        sekunde1 = random.randint(0,60)
        if sekunde1<10:
            sekunde1 = "0"+str(sekunde1)
        #datPocetka ="'"+str(godina1) + "-"+str(mesec1)+"-"+str(dan1)+" "+str(sati1)+":"+str(minuti1)+":"+str(sekunde1)+"'")
        godina2 = 2020
        dan2 = random.randint(1,32)
        mesec2 = random.randint(1,13)
        if (mesec2<=provera):
            mesec2 = provera+1
            

        if(mesec2 <10):
            mesec2 = "0"+str(mesec2)
        if(dan2 <10):
            dan2 = "0"+str(dan2)
        idSobe = str(i)
        datPocetka ="'"+str(godina1) + "-"+str(mesec1)+"-"+str(dan1)+" "+str(sati1)+":"+str(minuti1)+":"+str(sekunde1)+"'"
        datZavrsetka ="'"+str(godina2) +"-"+str(mesec2)+"-"+str(dan2)+" "+str("09")+":"+str("00")+":"+str("00")+"'"
        idGosta = brojac
        print("INSERT INTO domaci(datPocetka,datZavrsetka,gost_id,soba_id) VALUES ("+str(datPocetka)+","+str(datZavrsetka)+","+str(idGosta)+","+str(idSobe)+");")
        brojac = brojac - 1

tabelaGost()
print("___________________________________________________")
tabelaStrani()
print("___________________________________________________")
tabelaDomaci()
print("___________________________________________________")
tabelaHotel()
print("___________________________________________________")
tabelaVrstaSobe()
print("___________________________________________________")
tabelaSoba()
print("___________________________________________________")
tabelaIznajmljuje()
print("___________________________________________________")





















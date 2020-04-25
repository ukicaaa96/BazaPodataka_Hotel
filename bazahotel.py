import bs4
import requests
import random
import mysql.connector
import time

#TABELA GOST
def tabelaGost(mycursor):
    print("POPUNJAVANJE TABELE GOST")
    
    imena = ["Danilo", "Tina" , "Sasa" , "Ljiljana","Nena", "Petar", "Djordje", "Uros", "Igor", "Goran", "Zoran","Snezana"]
    prezimena = ["Markovic" , "Nikolic" , "Stefanovic" , "Gajic" , "Lazic", "Mitrovic" , "Jovic", "Ilic", "Jovicic", "Prlic"]

    straniImena = ["John" , "Garet" , "Ross", "Joey" , "Charlie" , "Jake", "Alan", "Chloe" , "Hana" , "Maria", "Jennifer"]
    straniPrezimena = ["Geler" , "Smith" , "Amstrong" , "Enderson" , "Hart" , "Barkley" , "Lindelof", "Durant"]
    
    for i in range(1,30):
        if(i%2 == 0):         
            JMBG = random.randint(100000000000000, 999999999999999)
            ime = random.choice(imena)
            prezime = random.choice(prezimena)
            komanda = "INSERT INTO gost (ime,prezime,JMBG) VALUES ( "+"'"+str(ime)+"'"+","+"'"+str(prezime)+"'"+","+"'"+str(JMBG)+"')"
            mycursor.execute(komanda)
            db.commit()
            print(komanda)
        else:
            JMBG = random.randint(100000000000000, 999999999999999)
            ime = random.choice(straniImena)
            prezime = random.choice(straniPrezimena)
            komanda = "INSERT INTO gost (ime,prezime,JMBG) VALUES ( "+"'"+str(ime)+"'"+","+"'"+str(prezime)+"'"+","+"'"+str(JMBG)+"')"
            mycursor.execute(komanda)
            db.commit()
            print(komanda)            
           
#TABELA DOMACI
def tabelaDomaci(mycursor):
    print("POPUNJAVANJE TABELE DOMACI")
    
    gradovi = ["Beograd" , "Jagodina" , "Arandjelovac" , "Kragujevac" , "Nis" , "Valjevo" , "Paracin" , "Novi Sad"]
    adrese = ["Branka Radicevica 8" , "Stevana Jakovljevica bb" , "Nikole Tesle 14" , "Omladinskih brigada 15" , "Kneza Lazara 22"]    
    for i in range (2,30,2):
        idGosta = str(i)
        grad = random.choice(gradovi)
        adresa = random.choice(adrese)
        komanda="INSERT INTO domaci (grad,adresa,gost_id) VALUES ("+"'"+str(grad)+"'"+","+"'"+str(adresa)+"'"+","+"'"+str(idGosta)+"'"+")"
        mycursor.execute(komanda)
        db.commit()
        print(komanda)
    print("")        
#TABELA STRANI       
def tabelaStrani(mycursor):
    print("POPUNJAVANJE TABELE STRANI")
    drzave = ["USA", "Engleska", "Kanada", "Nemacka", "Holandija", "Francuska"]
    for i in range(1,30,2):
        drzava = random.choice(drzave)
        pasos = random.randint(111111,999999)
        idGosta = i
        komanda="INSERT INTO strani (drzava,br_pasosa,gost_id) VALUES ("+"'"+str(drzava)+"'"+","+"'"+str(pasos)+"'"+","+"'"+str(idGosta)+"'"+")"
        mycursor.execute(komanda)
        db.commit()
        print(komanda)
    print("")
#TABELA HOTEL
def tabelaHotel(mycursor):
    print("POPUNJAVANJE TABELE HOTEL")
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
        broj = random.randint(1,5)
        if(broj == 1):
            podatak = str(broj) + " zvezdica"
        else:
            podatak = str(broj) + " zvezdice" 
        listaKategorija.append(podatak)

    #Popunjavamo tabelu hotel u nasoj bazi
    for i in range(len(listaKategorija)):
        komanda = "INSERT INTO hotel (naziv,kategorija) VALUES (" +"'"+listaHotelaFinal[i]+"'"+","+"'"+listaKategorija[i]+"'"+")"
        mycursor.execute(komanda)
        db.commit()
        print(komanda)
    print("")

#TABELA VRSTA_SOBE
def tabelaVrstaSobe(mycursor):
    print("POPUNJAVANJE TABELE VRSTA_SOBE")
    #Svaki hotel ima 3 vrste soba(Standard,Porodicni,Apartman)
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
        komanda = "INSERT INTO vrsta_sobe (opis,cenaDan) VALUES ("+"'"+str(opisi[i])+"'"+","+"'"+str(random.randint(100,230))+"'"+")"
        mycursor.execute(komanda)
        db.commit()
        print(komanda)
    print("")        
#TABELA SOBA
def tabelaSoba(mycursor):
    print("POPUNJAVANJE TABELE SOBA")
    #random biramo dodatni opis sobe
    dodatniOpisSobe = ["Soba je sa pogledom na planinu, poseduje bazen u dvoristu, garazu za automobil i djakuzi",
                   "Soba je sa pogledom na setaliste, velikom terasom i opremljenom kuhinjom",
                   "Soba je sa pogledom na dvoriste, tokom boravka u ovoj sobi ce biti promenjena posteljina na 5 dana",
                   "Soba poseduje Sony playstation 4, koji gosti mogu da igraju potpuno besplatno, dostupne igrice su (PES-20, FIFA 19 , Call of Duty, GTA V)",
                   "U ovoj sobi je dozvoljen pristup kucnim ljubimcima"
                   ]
    #nasumicno kreiramo ID za hotel i vrstu (id hotela i vrste moraju da postoje, nije moguce imati id hotela 10, ako imam samo 9 hotela u bazi)
    for i in range(1,30):
        id_hotela = random.randint(1,9)
        id_vrste = random.randint(1,3)
        opis = random.choice(dodatniOpisSobe) 
        #komanda za popunjavanje tabele SOBA
        komanda="INSERT INTO soba (opis,hotel_id,vrsta_id) VALUES ("+"'"+str(opis)+"'"+","+"'"+str(id_hotela)+"'"+","+"'"+str(id_vrste)+"'"+")"
        mycursor.execute(komanda)
        db.commit()
        print(komanda)
    print("")   
#TABELA IZNAJMLJUJE
def tabelaIznajmljuje(mycursor):
    print("POPUNJAVANJE TABELE IZNAJMLJUJE")
    brojac = 29
    #Dodajemo nulu ispred broja manjeg od 10 da bi bio ispravam format datuma i vremena npr (2020-02-04 13:04:33)
    for i in range(1,30):
        #Pocetak
        godina1 = 2020
        mesec1 = random.randint(1,9)
        provera = mesec1
        if mesec1<10:
            mesec1 = "0"+str(mesec1)  
        dan1 = random.randint(1,28)
        if dan1<10:
            dan1 = "0"+str(dan1)
        sati1 = random.randint(1,23)
        if sati1<10:
            sati1 = "0"+str(sati1)  
        minuti1 = random.randint(0,59)
        if minuti1<10:
            minuti1 = "0"+str(minuti1)
        sekunde1 = random.randint(0,59)
        if sekunde1<10:
            sekunde1 = "0"+str(sekunde1)

        #Zavrsetak 
        godina2 = 2020
        dan2 = random.randint(1,28)
        mesec2 = random.randint(1,12)
        if (mesec2<=provera):
            mesec2 = provera+1
        if(mesec2 <10):
            mesec2 = "0"+str(mesec2)
        if(dan2 <10):
            dan2 = "0"+str(dan2)
        idSobe = i
        idGosta = brojac
        datPocetka ="'"+str(godina1) + "-"+str(mesec1)+"-"+str(dan1)+" "+str(sati1)+":"+str(minuti1)+":"+str(sekunde1)+"'"
        datZavrsetka ="'"+str(godina2) +"-"+str(mesec2)+"-"+str(dan2)+" "+str("09")+":"+str("00")+":"+str("00")+"'"
        
        
        komanda = "INSERT INTO iznajmljuje (datumPocetka,datumZavrsetka,gost_id,soba_id) VALUES ("+str(datPocetka)+","+str(datZavrsetka)+","+"'"+str(idGosta)+"'"+","+"'"+str(idSobe)+"')"
        mycursor.execute(komanda)
        db.commit()
        print(komanda)
        brojac -= 1
    print("")


#__________________________________________________________

imeBaze = input("Unesite ime vase baze podataka: ")
passBaze = input("Unesite sifru: ")
print("Da li zelis da kreiras tabele:")
print("1.Da")
print("2.Ne")
izbor = int(input(">>>"))


db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = passBaze,
    database = imeBaze
    )

mycursor = db.cursor()



if (izbor == 1):
    tabelaGost = """CREATE TABLE gost (id_gosta INTEGER UNSIGNED AUTO_INCREMENT NOT NULL PRIMARY KEY,
    ime VARCHAR(50) NULL,
    prezime VARCHAR(50) NULL,
    JMBG VARCHAR(50) NULL
    )"""

    tabelaStrani = """CREATE TABLE strani (
    drzava VARCHAR(50) NULL,
    br_pasosa VARCHAR(10) NULL,
    gost_id INTEGER UNSIGNED NOT NULL ,
    FOREIGN KEY(gost_id) REFERENCES gost (id_gosta)
    )"""

    tabelaDomaci = """CREATE TABLE domaci (
    grad VARCHAR(50) NULL,
    adresa VARCHAR(80) NULL,
    gost_id INTEGER UNSIGNED NOT NULL ,
    FOREIGN KEY(gost_id) REFERENCES gost (id_gosta)
    )"""

    tabelaHotel = """CREATE TABLE hotel (
    id_hotela INTEGER UNSIGNED AUTO_INCREMENT NOT NULL PRIMARY KEY,
    naziv VARCHAR(50) NOT NULL,
    kategorija VARCHAR(50) NOT NULL 
    );"""

    tabelaVrstaSobe = """CREATE TABLE vrsta_sobe (
    id_vrste INTEGER UNSIGNED AUTO_INCREMENT NOT NULL PRIMARY KEY,
    opis TEXT NULL,
    cenaDan INTEGER NOT NULL
    )"""

    tabelaSoba = """CREATE TABLE soba (
    id_sobe INTEGER UNSIGNED AUTO_INCREMENT NOT NULL PRIMARY KEY,
    opis TEXT NULL,
    hotel_id INTEGER UNSIGNED NOT NULL,
    vrsta_id INTEGER UNSIGNED NOT NULL ,
    FOREIGN KEY(vrsta_id) REFERENCES vrsta_sobe (id_vrste),
    FOREIGN KEY(hotel_id) REFERENCES hotel (id_hotela)
    )"""

    tabelaIznajmljuje = """CREATE TABLE iznajmljuje (
    datumPocetka DATETIME NOT NULL,
    datumZavrsetka DATETIME NOT NULL,
    gost_id INTEGER UNSIGNED NOT NULL,
    soba_id INTEGER UNSIGNED NOT NULL,
    FOREIGN KEY(gost_id) REFERENCES gost (id_gosta),
    FOREIGN KEY(soba_id) REFERENCES soba (id_sobe)
    )"""



    #Kreiranje tabela
    mycursor.execute(tabelaGost)
    time.sleep(1)
    mycursor.execute(tabelaStrani)
    time.sleep(1)
    mycursor.execute(tabelaDomaci)
    time.sleep(1)
    mycursor.execute(tabelaHotel)
    time.sleep(1)
    mycursor.execute(tabelaVrstaSobe)
    time.sleep(1)
    mycursor.execute(tabelaSoba)
    time.sleep(1)
    mycursor.execute(tabelaIznajmljuje)


time.sleep(3)
#Upisivanje u tabele
tabelaGost(mycursor)
tabelaStrani(mycursor)
tabelaDomaci(mycursor)
tabelaHotel(mycursor)
tabelaVrstaSobe(mycursor)
tabelaSoba(mycursor)
tabelaIznajmljuje(mycursor)











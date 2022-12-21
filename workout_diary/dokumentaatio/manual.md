# **Workout diary käyttöohje**

Lataa käyttöösi ohjelman viimeisin [releasen](https://github.com/vtonteri/ot-harjoitustyo/releases) lähdekoodi, valitsemalla *Assets*-osion alta Source code

## **Ohjelman käynnistäminen**

Ennen ohjelman käynnistystä asenna riippuvuudet komennolla:

**poetry install**

- Ohjelma voidaan käynnistää menemällä *workout_diary* kansioon komentorivillä ja kirjoittamalla 

**poetry run invoke start**

- Vaihtoehtoinen tapa käynnistää, on mennä *workout_diary/src* -kansioon ja antaa komento:

**python3 main.py**

## **Kirjautuminen**

Ohjelma käynnistyy kirjautumisikkunaan:

![Kirjautumisikkuna](https://github.com/vtonteri/ot-harjoitustyo/blob/main/workout_diary/dokumentaatio/kirjautumisikkuna.jpg)

Käyttäjä kirjautuu ohjelmaan syöttämällä käyttäjätunnuksen ja salasanan, jonka jälkeen painetaan Login-nappia.

Ohjelma suljetaan painamalla stop application nappia.

Painamalla Create New User -nappia, käyttäjä voi luoda uuden käyttäjätunnuksen. Napin painamisen jälkeen aukeaa uuden käyttäjän luomiseen tarkoitettu ikkuna:

![Luo uusi käyttäjä](https://github.com/vtonteri/ot-harjoitustyo/blob/main/workout_diary/dokumentaatio/luo_uusi_kayttaja.jpg)

Ikkunassa käyttäjä määrittää itselleen käyttäjänimen sekä salasanan. Uusi käyttäjä luodaan painamalla Create new user -nappia. Näkymästä siirrytään takaisin kirjautumisikkunaan painamalla Exit-nappia. Tämän jälkeen käyttäjän pitää kirjautua ohjelmaan sisään. Käyttäjätunnuksen täytyy olla uniikki. Salasana tallennetaan tietokantaan salattuna. 

Sisäänkirjautumisen jälkeen käyttäjälle näytetään ohjelman päänäkymä:

![Päänäkymä](https://github.com/vtonteri/ot-harjoitustyo/blob/main/workout_diary/dokumentaatio/paanakyma.jpg)

Päänäkymässä on seuraavat toiminnallisuudet:
- Create new workout:
    - Käyttäjä voi luoda itselleen uudet harjoitusohjelmat
- Update workouts from database
    - Käyttäjä päivittää luomansa harjoitusohjelmat tietokannasta, jonka jälkeen niitä voi tarkastella päänäkymässä
- Select date
    - Käyttäjä valitsee minkä päivän harjoitusta hän haluaa tarkastella
- Näkymässä olevaan tekstilaatikkoon ilmestyy harjoitusohjelman tiedot
- Log out -nappia painamalla käyttäjä kirjautuu ulos ohjelmasta ja sovellus siirtyy kirjautumisikkunaan

![Päänäkymä](https://github.com/vtonteri/ot-harjoitustyo/blob/main/workout_diary/dokumentaatio/paanakyma_harjoitusohjelmalla.jpg)

![Päänäkymä](https://github.com/vtonteri/ot-harjoitustyo/blob/main/workout_diary/dokumentaatio/paanakyma_select_date.jpg)

- Uusi harjoitusohjelma luodaan napista Create new workout, jonka painamisen jälkeen aukeaa uuden harjoitusohjelman luontiin tarkoitettu ikkuna:

![Luo uusi harjoitusohjelma](ttps://github.com/vtonteri/ot-harjoitustyo/blob/main/workout_diary/dokumentaatio/luo_harjoitusohjelma.jpg)

Käyttäjä syöttää vapaisiin tekstikenttiin haluamansa tiedot ikkunassa annettujen määreiden mukaisesti:
- Workout name: Harjoitukselle annettava nimi, ei tarvitse olla uniikki
- Enter workout sets: harjoituksen aikana tehtävät sarjat tai muu määre
- Workout details: yksityiskohtaista tietoa harjoituksesta

Päivämäärä valitaan aukeavasta, erillisestä kalenterista.

Alasvetovalikoista valitaan harjoituksen toistuvuus:
- Weekly-valinta kopioi saman harjoituksen kolmelle viikolle (annettu päivämäärä + kaksi sitä seuraavaa viikkoa)

Alasvetovalikosta valitaan myös harjoituksen tyyppi. Tyypin valinnalla ei ohjelman tämän hetkisessä versiossa ole vaikutusta toimintoihin. 
- Lihaskuntoharjoitus (weight lifting)
- Kestävyysharjoitus (cardio)

Harjoitusohjelma luodaan painamalla Create new workout -nappia. Näkymä suljetaan painamalla Exit -nappia ja sovellus palaa takaisin päänäkymään.

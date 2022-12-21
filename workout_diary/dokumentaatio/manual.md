# **Workout diary käyttöohje**

Lataa käyttöösi ohjelman viimeisin [releasen](https://github.com/vtonteri/ot-harjoitustyo/releases) lähdekoodi, valitsemalla *Assets*-osion alta Source code

## **How to start the application**

Ennen ohjelman käynnistystä asenna riippuvuudet komennolla:

**poetry install**

- Ohjelma voidaan käynnistää menemällä *workout_diary* kansioon komentorivillä ja kirjoittamalla 

**poetry run invoke start**

- Vaihtoehtoinen tapa käynnistää, on mennä *workout_diary/src* -kansioon ja antaa komento:

**python3 main.py**

## **Kirjautuminen**

Ohjelma käynnistyy kirjautumisikkunaan:

!(https://github.com/vtonteri/ot-harjoitustyo/blob/main/workout_diary/dokumentaatio/kirjautumisikkuna.jpg)

Käyttäjä kirjautuu ohjelmaan syöttämällä käyttäjätunnuksen ja salasanan, jonka jälkeen painetaan Login-nappia.

Ohjelma suljetaan painamalla stop application nappia.

Painamalla Create New User -nappia, käyttäjä voi luoda uuden käyttäjätunnuksen. Napin painamisen jälkeen aukeaa uuden käyttäjän luomiseen tarkoitettu ikkuna:

!(https://github.com/vtonteri/ot-harjoitustyo/blob/main/workout_diary/dokumentaatio/luo_uusi_kayttaja.jpg)

Ikkunassa käyttäjä määrittää itselleen käyttäjänimen sekä salasanan. Uusi käyttäjä luodaan painamalla Create new user -nappia. Näkymästä siirrytään takaisin kirjautumisikkunaan painamalla Exit-nappia. Tämän jälkeen käyttäjän pitää kirjautua ohjelmaan sisään.

Sisäänkirjautumisen jälkeen käyttäjälle näytetään ohjelman päänäkymä:

!(https://github.com/vtonteri/ot-harjoitustyo/blob/main/workout_diary/dokumentaatio/paanakyma.jpg)

Päänäkymässä on seuraavat toiminnallisuudet:
- Create new workout:
    - Käyttäjä voi luoda itselleen uudet harjoitusohjelmat
- Update workouts from database
    - Käyttäjä päivittää luomansa harjoitusohjelmat tietokannasta, jonka jälkeen niitä voi tarkastella päänäkymässä
- Select date
    - Käyttäjä valitsee minkä päivän harjoitusta hän haluaa tarkastella
- Näkymässä olevaan tekstilaatikkoon ilmestyy harjoitusohjelman tiedot.

!(https://github.com/vtonteri/ot-harjoitustyo/blob/main/workout_diary/dokumentaatio/paanakyma_harjoitusohjelmalla.jpg)

!(https://github.com/vtonteri/ot-harjoitustyo/blob/main/workout_diary/dokumentaatio/paanakyma_select_date.jpg)



## **How to stop the application**

You can press *Stop application* button or just close the window.

## **How to run tests**

Tests can be run in the following way: 
- go to *workout_diary* -directory in a command shell or command prompt and type: **poetry run invoke test**

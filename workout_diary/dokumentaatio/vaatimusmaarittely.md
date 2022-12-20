# **Vaatimusmäärittely**

## **Sovelluksen tarkoitus**

Sovelluksen avulla käyttäjä voi tallentaa itselleen harjoitusohjelman. Sovellusta voi käyttää useampi rekisteröitynyt käyttäjä, joilla kaikilla on omat harjoitusohjelmansa.

## Käyttäjät

Sovelluksessa on seuraavat käyttäjäprofiilit:

- Peruskäyttäjä: sovelluksen käyttäminen, ei pääsyä tietokantoihin tai muiden käyttäjien tietoihin, muutoin kuin sovelluksen käyttöliittymän toiminnallisuuksien kautta.

## Käyttöliittymä

Kirjautumisikkuna:

![Käyttöliittymä, kirjautumisikkuna](https://github.com/vtonteri/ot-harjoitustyo/blob/main/workout_diary/dokumentaatio/kirjautumisikkuna.jpg)

Luo uusi käyttäjä -ikkuna

![Käyttöliittymä, luo uusi käyttäjä -ikkuna](https://github.com/vtonteri/ot-harjoitustyo/blob/main/workout_diary/dokumentaatio/luo_uusi_kayttaja.jpg)

Päänäkymä:

![Käyttöliittymä, päänäkymä](https://github.com/vtonteri/ot-harjoitustyo/blob/main/workout_diary/dokumentaatio/paanakyma.jpg)

Luo uusi harjoitusohjelma -ikkuna

![Käyttöliittymä, luo harjoitusohjelma -ikkuna](https://github.com/vtonteri/ot-harjoitustyo/blob/main/workout_diary/dokumentaatio/luo_harjoitusohjelma.jpg)

# Perusversion tarjoama toiminnallisuus

## Ennen kirjautumista

- Käyttäjä voi luoda itselleen käyttäjätunnuksen ja salasanan (Toteutettu, toimii)
    - Profiili tallennetaan tietokantaan ja käyttäjätunnuksen tulee olla uniikki.

- Käyttäjä voi kirjautua järjestelmään
    - Kirjautuminen tapahtuu ohjelman käynnistämisen jälkeen avautuvassa kirjautumisikkunassa
    - Jos salasana tai käyttäjätunnus ovat virheelliset, tai käyttäjätunnusta ei ole luotu, ilmoittaa ohjelma tästä ja palaa takaisin kirjautumisikkunaan

- Käyttäjä voi lopettaa ohjelman suorittamisen

## Kirjautumisen jälkeen

- Avautuvassa näkymässä (pääikkuna):
    - Käyttäjä voi siirtyä luomaan uusia harjoitusohjelmia
    - Tarkastella jo olemassa olevia harjoitusohjelmia
    - Kirjautua ulos

- Uuden harjoitusohjelman lisääminen tapahtuu "Create new workout" -painiketta painamalla
    - Uusi harjoitusohjelma sisältää seuraavat tiedot:
        - Harjoituksen nimi (merkkijono, vapaasti kirjoitettavissa)
        - Harjoituksen toistuvuus (weekly, None)
            - Mikäli valitaan "Weekly" harjoitusohjelma lisätään valitun päivämäärän lisäksi kahdelle seuraavalle viikolle
        - Harjoituksen tyyppi (Weight lifting / Cardio)
        - Harjoituksen toistot ja toistomäärät (sets)
        - Harjoituksen yksityiskohdat (Workout details):

- Lopuksi käyttäjä voi kirjautua ulos ohjelmasta

# **Jatkokehitysideoita**

Perusversion jälkeen sovellusta voidaan laajentaa esimerkiksi seuraavilla toiminnallisuuksilla:

- Harjoitusohjelmien muokkaaminen tallentamisen jälkeen
- Pääkäyttäjä-roolin lisääminen
    - Pääsy tietokantoihin ja käyttäjätietoihin käyttöliittymän kautta
- 
- Harjoitusohjelmien jakaminen muiden käyttäjien kanssa
- Ruokapäiväkirjan lisääminen osaksi harjoitusohjelmaa (painonpudotus, painon ylläpito ja lihasmassan kasvatus)


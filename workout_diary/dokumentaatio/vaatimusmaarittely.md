# **Vaatimusmäärittely**

## **Sovelluksen tarkoitus**

Sovelluksen avulla käyttäjä voi tallentaa itselleen harjoitusohjelman ja seurata sen toteutumista. Sovelluksen avulla voi seurata oman kunnon ja painon kehittymistä. Sovellusta voi käyttää useampi rekisteröitynyt käyttäjä, joilla kaikilla on omat harjoitusohjelmansa.

## Käyttäjät

Sovelluksessa on seuraavat käyttäjäprofiilit:

- Pääkäyttäjä: sovelluksen käyttäjien ja tietokantojen hallinta
- Peruskäyttäjä: sovelluksen käyttäminen, ei pääsyä tietokantoihin tai muiden käyttäjien tietoihin, muutoin kuin sovelluksen käyttöliittymän toiminnallisuuksien kautta

## Käyttöliittymäluonnos

![Käyttöliittymäluonnos](https://github.com/vtonteri/ot-harjoitustyo/blob/main/workout_diary/dokumentaatio/kayttoliittymaluonnos.jpg)

# Perusversion tarjoama toiminnallisuus

## Ennen kirjautumista

- Käyttäjä voi luoda itselleen käyttäjätunnuksen ja salasanan (Toteutettu, toimii)
    - Profiili tallennetaan tietokantaan ja käyttäjätunnuksen tulee olla uniikki. Käyttäjätunnuksen pitää olla vähintään viisi merkkiä pitkä, eikä se saa sisältää ääkkösiä tai erikoismerkkejä. (ei toteutettu)
- Pääkäyttäjälle on luotu erilliset tunnukset, joiden avulla pääkäyttäjä pääsee näkemään kaikkien käyttäjien profiilitiedot sekä tallennetut harjoitusohjelmat (ei toteutettu)

- Käyttäjä voi kirjautua järjestelmään (Toteutettu, toimii)
    - Kirjautuminen tapahtuu ohjelman käynnistämisen jälkeen avautuvassa kirjautumisikkunassa
    - Pääkäyttäjä kirjautuu järjestelmään samaa toiminnallisuutta käyttäen
    - Jos salasana tai käyttäjätunnus ovat virheelliset, tai käyttäjätunnusta ei ole luotu, ilmoittaa ohjelma tästä ja palaa takaisin kirjautumisikkunaan

## Kirjautumisen jälkeen

- Avautuvassa näkymässä näytetään yksityiskohtainen näkymä meneillään olevasta päivästä sekä joko viikko- tai kuukausinäkymä (Ei toteutettu)
    - Meneillään olevan päivän yksityiskohtainen näkymä on sijoitettu avautuneen ikkunan yläosaan
    - Viikko- tai kuukausinäkymä on sijoitettu avautuneen ikkunan alaosaan (toteutettu)
    - Viikko- tai kuukausinäkymä voidaan valita avautuneen ikkunan alaosassa olevasta valintapainikkeesta
- Kalenterissa näytetään harjoitusohjelma, joka voidaan valita ja avautuvasta näkymästä tarkastella harjoitusta (Ei toteutettu)
- Uuden harjoitusohjelman lisääminen tapahtuu "Add" -painiketta painamalla (Toteutettu, toimii)
    - Uusi harjoitusohjelma sisältää seuraavat tiedot:
        - Harjoituksen nimi (merkkijono, vapaasti kirjoitettavissa)
        - Harjoituksen toistuvuus
        - Harjoituksen tyyppi (Weight lifting / Cardio)
            - Vaikuttaa seuraaviin valintoihin
        - Harjoituksen yksityiskohdat (Workout details):
            - Weight lifting:
                - Ylläpito vai kehitys
                    - Kehitys: valitaan kuinka monta prosenttia sarjojen painoja kasvatetaan viikkotasolla
                        - Ohjelma laskee sarjojen painot harjoituksiin
                    - Ylläpito: sarjojen painoja ei kasvateta
                - Harjoituksen toistuvuus
                    - Valittavissa
                        - Weekly
                            - Kuinka monta kertaa viikossa
                            - Päivät
                        - Monthly
                            - Kuinka monta kertaa kuukaudessa
                            - Millä viikolla
                            - Minä viikonpäivänä
            - Sarjan nimi (Set) 
                    - Toistomäärät (Repetitions)
                    - Paino (Weight)
            - Cardio:
                - Harjoituksen tyyppi (Running, Cycling, Swimming, Walking etc.)
                - Harjoituksen kesto (HH:MM)
                - Sykealue (BPM)
- Harjoitusohjelman muokkaaminen: (ei toteutettu)
    - Harjoitusohjelman saa auki valitsemalla aloitusnäkymässä näkyvistä harjoituksista niiden tiedot
    - Avautuvasta ikkunasta voidaan muokata harjoituksen tietoja

- Harjoitusohjelman toteutuminen (ei toteutettu)
    - Avautuvasta ikkunasta voidaan valita toteutuiko päivän harjoitus suunnitellusti
    - Mikäli muutoksia harjoituksen sisältöön, voidaan valita "Edit", jonka jälkeen muutokset voidaan kirjata harjoituksen kohdalle

- Lopuksi käyttäjä voi kirjautua ulos ohjelmasta (Toteutettu, toimii)

# **Jatkokehitysideoita**

Perusversion jälkeen sovellusta voidaan laajentaa esimerkiksi seuraavilla toiminnallisuuksilla:

- Harjoitusohjelmien jakaminen muiden käyttäjien kanssa
- Ruokapäiväkirjan lisääminen osaksi harjoitusohjelmaa (painonpudotus, painon ylläpito ja lihasmassan kasvatus)


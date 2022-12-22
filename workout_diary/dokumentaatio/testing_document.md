# Testausdokumentti

Ohjelmaa on testattu itse kirjoitettujen yksikkötestien avulla sekä järjestelmätasolla manuaalisesti ohjelmaa käyttämällä.

# Yksikkö- ja integraatiotestaus

## Sovelluslogiikka 

Sovelluslogiikka testataan `workout_service_test` sekä `user_service_test` luokilla. Molemmissa luokissa luodaan tarvittavat oliot testaamista varten.

## Repositorio-luokat

Tietojen tallennuksen testaus toteutetaan luokkien `workout_repository_test` sekä `user_repository_test` toimesta. Molemmissa luokissa testataan tietojen tallennus sekä hakeminen tietokantaan ja tietokannasta.

## Testauskattavuus

Käyttöliittymään liittyvää koodia lukuun ottamatta, testauksen haarautumakattavuus on 82 %.

![Testauskattavuus](https://github.com/vtonteri/ot-harjoitustyo/blob/main/workout_diary/dokumentaatio/testikattavuus.jpg)

Testaamatta jäävät `main.py`, `initialize_database.py` sekä `database_connection.py`. Testaamatta jäivät myös osa reposotorioiden toiminnoista sekä osa `user_service` luokan metodeista.

## Järjestelmätestaus

Järjestelmä on testattu manuaalisesti.

## Asennus ja konfigurointi

Ohjelman asennus ja käyttö on testattu Windows 11 käyttöjärjestelmällä.

## Toiminnallisuudet

Määrittelydokumentissa kuvatut toiminnallisuudet on testattu järjetelmätestauksen yhteydessä. Eri virhetilanteita on testattu väärillä syötteillä.

## Sovellukseen jääneet laatuongelmat

- Järjestelmä ei anna virheilmoitusta, mikäli käyttäjätunnus on jo käytössä.
- Järjestelmä ei indikoi, mikäli workout_id:n luominen ei onnistu
- Järjestelmä ei indikoi, mikäli harjoitusohjelmaa ei kyetä luomaan (esimerkiksi puutteellisesti täytetyt tiedot kentissä)
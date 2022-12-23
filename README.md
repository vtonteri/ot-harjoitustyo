# **Workout Diary**

Ohjelman avulla käyttäjä voi tallentaa ja katsella omia harjoituksiaan.

## **Huomioita Python-versioista**

Ohjelma on testattu ja toiminta varmistettu Python 3.9.7 -versiolla. Aiempien versioiden kanssa toimintaa ei voida taata.

## **Dokumentaatio**

**[Käyttöohje](https://github.com/vtonteri/ot-harjoitustyo/blob/main/workout_diary/dokumentaatio/manual.md)**

**[Vaatimusmäärittely](https://github.com/vtonteri/ot-harjoitustyo/blob/main/workout_diary/dokumentaatio/vaatimusmaarittely.md)**

**[Testausdokumentti](https://github.com/vtonteri/ot-harjoitustyo/blob/main/workout_diary/dokumentaatio/testing_document.md)**

**[Tuntikirjanpito](https://github.com/vtonteri/ot-harjoitustyo/blob/main/workout_diary/dokumentaatio/tuntikirjanpito.md)**

**[Muutosloki](https://github.com/vtonteri/ot-harjoitustyo/blob/main/workout_diary/dokumentaatio/changelog.md)**

**[Arkkitehtuurikuvaus](https://github.com/vtonteri/ot-harjoitustyo/blob/main/workout_diary/dokumentaatio/architecture.md)**

# **Workout diary käyttöohje**

Lataa käyttöösi ohjelman viimeisin [releasen](https://github.com/vtonteri/ot-harjoitustyo/releases) lähdekoodi, valitsemalla *Assets*-osion alta Source code

## **Asennus**

1. Alusta tietokanta komennolla:

`poetry run invoke build`

2. Asenna riippuvuudet komennolla:

`poetry install`

4. Ohjelma voidaan käynnistää menemällä *workout_diary* kansioon komentorivillä ja kirjoittamalla 

`poetry run invoke start`

5. Vaihtoehtoinen tapa käynnistää, on mennä *workout_diary/src* -kansioon ja antaa komento:

`poetry python3 main.py`

## **Komentorivitoiminnot**

1. Tietokannan alustaminen

`poetry run invoke build`

2. Käynnistäminen

`poetry run invoke start`

3. Testaus 

`poetry run invoke test`

4. Testikattavuus

`poetry run invoke coverage-report`

Raportti löytyy *htmlcov* hakemistosta

5. Pylint

`poetry run invoke lint`

## **Releases**

**[Release, week 5](https://github.com/vtonteri/ot-harjoitustyo/releases/tag/viikko5)**

**[Release, week 6](https://github.com/vtonteri/ot-harjoitustyo/releases/tag/Viikko6)**

**[Final release, week 7](https://github.com/vtonteri/ot-harjoitustyo/releases/tag/Viikko7)**
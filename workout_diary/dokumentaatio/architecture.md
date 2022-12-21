# **Arkkitehtuurikuvaus**

## **Rakenne**

Ohjelma noudattaa kolmitasoista kerrosarkkitehtuuria. Koodin pakkausrakenne on seuraavanlainen: 

![Pakkausrakenne](https://github.com/vtonteri/ot-harjoitustyo/blob/main/workout_diary/dokumentaatio/arkkitehtuuri_pakkausrakenne.jpg)

Pakkaus UI sisältää kaikki käyttöliittymään liittyvän koodin. Services -pakkaus sisältää sovelluslogiikkaan liittyvän koodin. Repository pakkaus sisältää tietokantaan liittyvän koodin. Entities sisältää koodin, joka kuvaa ohjelman käyttämien tietokohteita. 

## **Käyttöliittymä**

Käyttöliittymä sisältää neljä eri näkymää:
- Kirjautuminen
- Uuden käyttäjän luominen
- Päänäkymä
- Uuden harjoitusohjelman luominen

Jokainen näkymistä on toteutettu omana luokkanaan. Ainoastaan yksi näkymistä on kerrallaan näkyvissä. Niiden näyttämisestä vastaa UI-luokka. Käyttöliittymä on pyritty eristämään sovelluslogiikasta, se kutsuu ainoastaan [workout service](https://github.com/vtonteri/ot-harjoitustyo/blob/main/workout_diary/src/services/workout_service.py) ja [user service](https://github.com/vtonteri/ot-harjoitustyo/blob/main/workout_diary/src/services/user_service.py) -luokan metodeja.

Tekstikentät tyhjennetään, kun tarvittava tieto on tallennettu tietokantaan
- Luo uusi käyttäjä -toiminnallisuuden jälkeen
- Luo uusi harjoitusohjelma -toiminnallisuuden jälkeen

Kun päänäkymässä painetaan nappia Update workouts from database, kutsutaan metodia [get_workouts](https://github.com/vtonteri/ot-harjoitustyo/blob/main/workout_diary/src/services/workout_service.py#L30)



## **Sovelluslogiikka**

Ohjelman loogisen tietomallin muodostavat luokat [User](https://github.com/vtonteri/ot-harjoitustyo/blob/main/workout_diary/src/entities/user.py) ja [Workout](https://github.com/vtonteri/ot-harjoitustyo/blob/main/workout_diary/src/entities/workout.py)




![Architecture](https://github.com/vtonteri/ot-harjoitustyo/blob/main/workout_diary/dokumentaatio/architecture.png)
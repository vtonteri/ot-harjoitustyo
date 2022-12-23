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

Kun päänäkymässä painetaan nappia Update workouts from database, kutsutaan metodia [get_workouts](https://github.com/vtonteri/ot-harjoitustyo/blob/main/workout_diary/src/services/workout_service.py#L27)


## **Sovelluslogiikka**

Ohjelman loogisen tietomallin muodostavat luokat [User](https://github.com/vtonteri/ot-harjoitustyo/blob/main/workout_diary/src/entities/user.py) ja [Workout:](https://github.com/vtonteri/ot-harjoitustyo/blob/main/workout_diary/src/entities/workout.py)

![Tietomalli](https://github.com/vtonteri/ot-harjoitustyo/blob/main/workout_diary/dokumentaatio/tietomalli.jpg)

Toiminnallisista kokonaisuuksista vastaavat [user service](https://github.com/vtonteri/ot-harjoitustyo/blob/main/workout_diary/src/services/user_service.py) sekä [workout service](https://github.com/vtonteri/ot-harjoitustyo/blob/main/workout_diary/src/services/workout_service.py). Luokat tarjoavat käyttöliittymän kaikille toiminnoille omat metodit, joita ovat esimerkiksi:

- `login_user(username, password)`
- `create_user(username, password`
- `hash_password(password)`
- `get_logged_in_username()`
- `create_workout(username, workout_name, date_and_time, repetition, workout_type, sets, details)`
- `get_workouts(username)`

User service pääsee käsiksi käyttäjän tietoihin tietojen tallennuksesta vastaavan, pakkauksessa *repositories*, sijaitsevien luokkien [user_repository](https://github.com/vtonteri/ot-harjoitustyo/blob/main/workout_diary/src/repositories/user_repository.py) ja [workout_repository](https://github.com/vtonteri/ot-harjoitustyo/blob/main/workout_diary/src/repositories/workout_repository.py). Workout service pääsee käsiksi sisäänkirjautuneen käyttäjän harjoitusohjelmiin 

- `WorkoutService` ja `UserService` -luokkien ja ohjelman muiden osien suhdetta kuvaava luokka/pakkauskaavio:

![Pakkauskaavio](https://github.com/vtonteri/ot-harjoitustyo/blob/main/workout_diary/dokumentaatio/pakkauskaavio.jpg)


## **Tietojen pysyväistallennus**

Pakkauksen *repositories* luokat `WorkoutRepository` ja `UserRepository` vastaavat tietojen tallentamisesta SQLite-tietokantaan. Molemmat luokat tallentavat tiedot eri tauluihin. Käyttäjän tiedot tallennetaan `users` tauluun ja harjoitusohjelman tiedot `workouts` tauluun, jotka alustetaan ennen ohjelman ensimmäistä käynnistämistä, suorittamalla `poetry run invoke build`. Luokat noudattavat Repository-suunnittelumallia ja ne voidaan tarvittaessa korvata uusilla toteutuksilla.


## **Päätoiminnallisuudet**

Kuvataan seuraavaksi ohjelman päätoiminnallisuudet sekvenssikaavioilla.


### **Käyttäjän sisäänkirjautuminen**

![Sisäänkirjautuminen](https://github.com/vtonteri/ot-harjoitustyo/blob/main/workout_diary/dokumentaatio/login_flowchart.jpg)

Käyttäjä kirjoittaa kenttiin omat tunnuksensa, joiden jälkeen tapahtumankäsittelijä selvittää, löytyykö tietokannasta kyseiset tunnukset. Salasanan tarkastus tapahtuu erillisen `check_password` metodin avulla. Salasana on tallennettu salattuna tietokantaan.

### **Uuden käyttäjän luominen**

![Uuden käyttäjän luominen](https://github.com/vtonteri/ot-harjoitustyo/blob/main/workout_diary/dokumentaatio/create_user_flowchart.jpg)

Käyttäjän syötettyä haluamansa käyttäjätunnuksen ja salasanan, tarkistetaan tietokannasta, onko tallennettuna samalla käyttäjätunnuksella, mikäli on, antaa ohjelma virheilmoituksen käyttäjälle. Mikäli käyttäjätunnusta ei ole vielä käytössä, luodaan uusi käyttäjätunnus ja salasana. Salasana salataan, ennen sen tallentamista tietokantaan, käyttäen `hash_password` metodia.

### **Uuden harjoitusohjelman luominen**

![Uuden harjoitusohjelman luominen](https://github.com/vtonteri/ot-harjoitustyo/blob/main/workout_diary/dokumentaatio/create_workout_flowchart.jpg)

Käyttäjä syöttää harjoitusohjelmansa tiedot kenttiin, jonka jälkeen harjoitusohjelmalle määritetään uusi `workout_id` käyttäen `random.randint`-metodia. Saatu kokonaisluku tarkastetaan tietokannasta, ja mikäli se on jo käytössä, arvotaan uusi. Id:n määrittämisen jälkeen harjoitusohjelma tallennetaan tietokantaan. 


## **Ohjelmaan rakenteeseen jääneet heikkoudet**

- Virheiden käsittelyä ei ole toteutettu kaikilta osin.
    - Käyttäjän antamien virheellisten syötteiden virheilmoitusten näyttäminen ei kaikilta osin toimi
- Osa UserServicen ja WorkoutServicen vastuulla olevista toiminnallisuuksista on toteutettu UI:n puolella
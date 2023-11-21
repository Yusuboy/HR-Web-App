# HR-WEB-APP
## Kuvaus
HR-Web-App on sovellus, joka tarjoaa tehokkaan ja käyttäjäystävällisen tavan seurata työntekijöiden läsnäoloa ja työaikoja organisaatiossasi. Sovellus tarjoaa seuraavia keskeisiä toimintoja:
- Läsnäolon seuranta: Työntekijät voivat kirjata sisään ja ulos, ja järjestelmä tallentaa automaattisesti työpäivien keston.
- Työaikojen seuranta: Sovellus tallentaa työntekijöiden työskentelytunnit, tauot ja poissaolot.
- Päivittäinen leimaus: Työntekijät voivat tehdä päivittäisiä leimauksia työpäivän alussa ja lopussa, mikä helpottaa tarkkaa ajanseurantaa.
- Admin/HR Läsnäolo seuranta: Seuraa työntekijöiden työaikoja, läsnäoloa ja taukoja, mikä helpottaa aikataulujen seurantaa ja hallintaa.
- Lomien hallinta: Työntekijät voivat pyytää lomia, ja esimiehet voivat tehokkaasti hyväksyä tai hylätä pyynnöt, mikä auttaa ylläpitämään tasapainoista henkilöstöä.

## Valmiina

- Käyttäjän kirjautuminen:
Käyttäjä voi kirjautua sisään aloitussivulla antamalla käyttäjätunnuksensa ja salasanansa.

- Uuden käyttäjän rekisteröityminen:
Käyttäjä voi luoda uuden tilin rekisteröitymissivulla antamalla käyttäjätunnuksensa ja salasanansa.

- Työajanseuranta:
käyttäjä voi kykenee sisään- ja ulosleimaukseen.

- Käyttäjän kotisivu:
Näytetään käyttäjän kotisivulla tietoja ja mahdollisuus kirjautua sisään ja ulos.

- Käyttäjäprofiilisivu:
Käyttäjä voi tarkastella työajanhistoriaansa päivämäärän ja keston mukaan.

- Uloskirjautuminen:
Käyttäjä voi kirjautua ulos käyttäjän kotisivulla.

- Ohjaus rekisteröitymisen jälkeen:
Uuden käyttäjän rekisteröitymisen jälkeen käyttäjä ohjataan takaisin aloitussivulle.

- Takaisin-painike käyttäjäprofiilisivulla:
Käyttäjä voi palata takaisin kotisivulle käyttäjäprofiilisivulla.


## Testaaminen tuotannossa

1. Clone the repository to your device and go to the root directory.
```
git clone git@github.com:Yusuboy/HR-Web-App.git
```

2. Create .env-file to project root with following contents
(your_db_name and your_secret_key can be chosen freely at this point):
```
DATABASE_URL="postgresql:///your_db_name"
>SECRET_KEY="your_secret_key"
```

3. Activate the virtual environment and install the requirements in root directory.
```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

4. Set the database schema. Note that you will need to have psql database running
```
psql < schema.sql
```

5.  Run the application using the command:
```
flask run
```
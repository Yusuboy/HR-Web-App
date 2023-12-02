# HR-WEB-APP
## Kuvaus
HR-Web-App on sovellus, joka tarjoaa tehokkaan ja käyttäjäystävällisen tavan seurata työntekijöiden läsnäoloa ja työaikoja organisaatiossasi. Sovellus tarjoaa seuraavia keskeisiä toimintoja:
- Läsnäolon seuranta: Työntekijät voivat kirjata sisään ja ulos, ja järjestelmä tallentaa automaattisesti työpäivien keston.
- Työaikojen seuranta: Sovellus tallentaa työntekijöiden työskentelytunnit, tauot ja poissaolot.
- Päivittäinen leimaus: Työntekijät voivat tehdä päivittäisiä leimauksia työpäivän alussa ja lopussa, mikä helpottaa tarkkaa ajanseurantaa.
- Admin/HR Läsnäolo seuranta: Seuraa työntekijöiden työaikoja, läsnäoloa ja taukoja, mikä helpottaa aikataulujen seurantaa ja hallintaa.
- Lomien hallinta: Työntekijät voivat pyytää lomia, ja esimiehet voivat tehokkaasti hyväksyä tai hylätä pyynnöt, mikä auttaa ylläpitämään tasapainoista henkilöstöä.

## Valmiina

- Käyttäjän kirjautuminen (User Login):
Käyttäjä voi kirjautua sisään aloitussivulla antamalla käyttäjätunnuksensa ja salasanansa.

- Uuden käyttäjän rekisteröityminen (User Registration):
Käyttäjä voi luoda uuden tilin rekisteröitymissivulla antamalla käyttäjätunnuksensa ja salasanansa.
- Työajanseuranta (Time Tracking):
Käyttäjä voi leimata sisään ja ulos.
Käyttäjä voi lisätä syyn ulosleimauksen ja sisäänleimauksen yhteydessä.

- Käyttäjän kotisivu (User Home Page):
Näytetään käyttäjän kotisivulla tietoja ja mahdollisuus kirjautua sisään, ulos, leimata työaikaa, tehdä lomahakemus ja lisätä syyn leimauksen yhteydessä.

- Käyttäjäprofiilisivu (User Profile Page):
Käyttäjä voi tarkastella työajanhistoriaansa päivämäärän, keston, sisään- ja ulosleimausten aikojen sekä leimauksiin liitettyjen syiden mukaan.

- Uloskirjautuminen (Logout):
Käyttäjä voi kirjautua ulos käyttäjän kotisivulla.

- Lomahakemus (Leave Request):
Käyttäjä voi tehdä lomahakemuksen, ja tämä näkyy käyttäjäprofiilisivulla.

- Navigointi (Navigation):
käyttäjä voi hinosti navigoida eri sivustojen välillä.


## Vielä tehtävänä

- Admin tili, joka hallinnoi työntekijöitä.
- Palkkalaskenta


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
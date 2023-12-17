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
Käyttäjä voi lisätä syyn sisäänleimaus ja ulosleimauksen yhteydessä.
- Käyttäjän kotisivu (User Home Page):
Näytetään käyttäjän kotisivulla tietoja ja mahdollisuus kirjautua sisään, kirjautua ulos, tehdä lomahakemus ja päästä tarkastelemaan työaika profiiliaan.

- Käyttäjäprofiilisivu (User Profile Page):
Käyttäjä voi tarkastella työajanhistoriaansa päivämäärän, keston, sisään- ja ulosleimausten aikojen. Lisäksi näytetään ansaittu palkka.

- Uloskirjautuminen (Logout):
Käyttäjä voi kirjautua ulos käyttäjän kotisivulla.

- Lomahakemus (Leave Request):
Käyttäjä voi tehdä lomahakemuksen, ja tämä näkyy käyttäjäprofiilisivulla. Käyttäjän lomahakemukset näkyvät samalla sivulla ja ne ovat värikoodattuja: Keltainen (pending), vihreä (approved) ja punainen (rejected).

- Navigointi (Navigation):
Käyttäjä voi helposti navigoida eri sivustojen välillä.

- Palkka (Salary):
Jokaisella työntekijällä on 12 dollarin tuntipalkka.

- Admin/HR - käyttäjä:
Admin-käyttäjään voidaan kirjautua käyttäjänimellä: Admin ja salasanalla: 123456. Admin-käyttäjä ohjataan dashboard-sivustolle kirjauduttuaan sisään. Dashboard-sivulla Admin näkee kaikki loma-anomukset sekä kaikkien työntekijöiden työhistorian. Admin voi hyväksyä tai hylätä lomahakemuksia, ja päätökset päivittyvät myös työntekijöille.








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
$ psql < drop_tables.sql
$ psql < schema.sql
```

5. Add Employees to the database. Note that this is optional but recommended
```
$ psql < insert_information.sql
```
5.  Run the application using the command:
```
$ flask run
```
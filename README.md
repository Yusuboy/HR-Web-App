# HR-WEB-APP
## Kuvaus
HR-Web-App on sovellus, joka tarjoaa tehokkaan ja käyttäjäystävällisen tavan seurata työntekijöiden läsnäoloa ja työaikoja organisaatiossasi. Sovellus tarjoaa seuraavia keskeisiä toimintoja:
- Läsnäolon seuranta: Työntekijät voivat kirjautua sisään ja ulos, järjestelmästä.
- Työaikojen seuranta: Sovellus tallentaa työntekijöiden työskentelytunnit sekä siihen liittyvät palkat, tauot ja poissaolot.
- Päivittäinen leimaus: Työntekijät voivat tehdä päivittäisiä leimauksia työpäivän alussa ja lopussa, mikä helpottaa tarkkaa ajanseurantaa.
- Admin/HR Läsnäolo seuranta: Seuraa työntekijöiden työaikoja, läsnäoloa ja taukoja, mikä helpottaa aikataulujen seurantaa ja hallintaa. Voi seurata myös työntekijöiden tuoloja.
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
Käyttäjä voi tehdä lomahakemuksen/ilmoittaa poissaolosta, ja tämä näkyy käyttäjäprofiilisivulla. Käyttäjän lomahakemukset näkyvät samalla sivulla ja ne ovat värikoodattuja: Keltainen (pending), vihreä (approved) ja punainen (rejected).

- Navigointi (Navigation):
Käyttäjä voi helposti navigoida eri sivustojen välillä.

- Palkka (Salary):
Jokaisella työntekijällä on 12 euron tuntipalkka.

- Admin/HR - käyttäjä:
Admin-käyttäjään voidaan kirjautua käyttäjänimellä: Admin ja salasanalla: 123456. Tämä edustaa ainoaa hallinto- ja henkilöstöhallinnon käyttäjätiliä, jolla on hallinnolliset oikeudet; uusia tällaisia ei voida luoda. Admin-käyttäjä ohjataan dashboard-sivustolle kirjauduttuaan sisään. Dashboard-sivulla Admin näkee kaikki loma-anomukset sekä kaikkien työntekijöiden työhistorian. Admin voi hyväksyä tai hylätä lomahakemuksia, ja päätökset päivittyvät myös työntekijöille. On vain yksi


## Kehitysideoita


- Nykyisellään admin näkee lomahakemukset ja pystyy niihin vastaamaan. Tulevaisuudessa tavoitteena on mahdollistaa myös lomahakemusten poistaminen adminille vastaamisen jälkeen. Tällä hetkellä admin voi poistaa lomahakemuksia, mutta ne ilmestyvät takaisin sivun päivittämisen yhteydessä.

- Erilaiset tuntipalkat ovat suunnitteilla. Pyhäpäivien palkka voisi olla korkeampi, esimerkiksi tuplapalkka normaalipäiviin verrattuna.


- Viestintä Adminin ja työntekijöiden välillä: Nykyisessä versiossa Admin voi vastata työntekijöiden lomahakemuksiin, mutta tulevaisuuden kehityssuunnitelmiin voisi sisältyä tehokkaampi viestintäkanava näiden kahden käyttäjäryhmän välille. 


## SOVELLUS EI OLE SAATAVILLA FLY.IO:SSA




## Testaaminen tuotannossa

1. Kloonaa repositorio koneellesi ja siirry juurikansioon.
```
git clone git@github.com:Yusuboy/HR-Web-App.git
```

2. Luo .env-tiedosto projektin juureen, ja määritä sen sisältö seuraavanlaiseksi::
```
DATABASE_URL=<tietokannan-paikallinen-osoite>
SECRET_KEY=<salainen-avain>
```

3. Siirry virtuaaliympäristöön ja asenna vaatimukset juurikansioon.
```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

4. Määritä tietokannan skeema. Huomaa, että psql-tietokannan on oltava käynnissä.
```
$ psql < drop_tables.sql
$ psql < schema.sql
```

5. Lisää työntekijöitä tietokantaan.
```
$ psql < insert_information.sql
```
6.  Käynnistä sovellus komennolla:
```
$ flask run
```

Sovelluksessa on käytetty kielimallia chatgpt.

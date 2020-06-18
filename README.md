# jsoric.github.io

Infinity travel agency je agencija za putovanja koja na **Pocetnoj stranici** prikazuje trenutne ponude sa cijenom, vrstom prijevoza i lokacijom na koje vršimo rezervacije putovanja. 


- **--** Sastoji se od pet stranica
- **--** Na Početnoj stranici su lokacije na koje agencija vrši putovanja, sa slikama, cijenom i kratkim opisom.
- **--** Na O Nama stranici je kratak opis naše tvrtke.
- **--** Na Galerija stranici su slike sa putovanja.
- **--** Na Registracija stranici je forma za registraciju putnika.
- **--** Na Prijava stranici je forma za prijavu prethodno registriranog korisnika.
- **--** Na Admin Prijava stranici je forma za prijavu admina koji može vidjeti tko se sve registrira.
** **

Upute za instalaciju za windows korisnike

- **--** Preuzmi repozitorij

- **--** Kreiraj virtualnu okolinu I preuzmi programe u powershellu naredbom:

 **python -m venv venv**

 **venv\Scripts\Activate.ps1**

 **pip install -r requirements.txt**

 **$env:FLASK_APP = ”app.py”**

 **set FLASK\_APP=app.py**

 **$env:FLASK\_DEBUG = 1**

- **--** Pokreniti aplikaciju naredbom **flask run**
- **--** Na web browser upisati [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

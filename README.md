## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

## Déploiement

### Liens

Compte collaborateur disponible :
- Email : mlc.sentry.sharing@gmail.com
- Password : Openclassrooms.123

Repo :
- CircleCi : [CircleCi p13_orange_county_lettings](https://app.circleci.com/pipelines/github/MatthLC/p13_orange_county_lettings)
- Docker : [Docker tags](https://hub.docker.com/r/matthlc92/oc-lettings-docker-build/tags)
- Heroku (se connecter avec le compte ci-dessus) : [Heroku oc-lettings-1337](https://dashboard.heroku.com/apps/oc-lettings-1337)
- Sentry (se connecter avec le compte ci-dessus) : [Sentry oc-lettings-sentry](https://sentry.io/organizations/student-x52/issues/)
- Application en production : 
  - [oc-lettings-1337](https://oc-lettings-1337.herokuapp.com/)
  - [oc-lettings-1337 Admin](https://oc-lettings-1337.herokuapp.com/admin/)
  - [oc-lettings-1337 Sentry debug](https://oc-lettings-1337.herokuapp.com/sentry-debug/)


### Conception
![schema_deploy](https://user-images.githubusercontent.com/85108007/175058909-d16d216b-7e44-4a42-ad4b-31362c1eaa8a.PNG)

Orange County Letting est une application développée avec Django et partagée via GitHub. A chaque commit réalisé, CircleCI exécutera le script `config.yml` présent dans le dossier `.circle`.

Route du déploiement :
1. GitHub : Commit
2. CircleCI : Exécution du script .circleci/config.yml
3. CircleCI/Script (Toutes les branches ) : installation de l'environnement Python et lancement des tests & flake8
4. CircleCI/Script (Branche main seulement) : installation de Docker et Build/Push de l'image vers le compte Docker à partir du Dockerfile
5. CircleCI/Script (Branche main seulement) : Installation Heroku et déploiement de l'image vers Heroku pour éxécution
6. Sentry : Surveillance de l'application en production sur Heroku

Le déploiement est entièrement automatisé

### Modifications

- Docker : Dockerfile
- CircleCI : /.circleci/config.yml
  - Lancement des tests & flake 8, Job : test_and_lint
  - Build & push de l'image vers Docker, Job : docker_build_and_push
  - Déploiement vers Heroku, Job : deploy_to_heroku
- Sentry : /oc_lettings_site/settings.py
  - sentry_sdk (Une variable d'environnement est utilisée afin de masquer la clé)

#### Variables d'environnement 
Toutes les variables devant être masquées se trouvent sur CircleCi en tant que variables d'environnement dédiées au projet `p13_orange_county_lettings`.

| Variable | Description |
| :---: | :---: |
| DOCKER_LOGIN | Email de connection Docker |
| DOCKER_PASSWORD | Mot de pass de connection Docker |
| IMAGE_NAME | Nom de l'image sur Docker : oc-lettings-docker-build |
| HEROKU_API_KEY | Clé API Heroku |
| HEROKU_APP_NAME | Nom de l'application sur Heroku : oc-lettings-1337 |
| SECRET_KEY | Clé Django |
| SENTRY_DNS | DNS Sentry |
| DEBUG | DEBUG de Django initialisé à False |

### Lancement d'une image Docker [Docker tags](https://hub.docker.com/r/matthlc92/oc-lettings-docker-build/tags)

Pour lancer une image en local :
```
tagname est le tag de l'image 
docker run -d -p 8000:8000 matthlc92/oc-lettings-docker-build:tagname

exemple:
docker run -d -p 8000:8000 matthlc92/oc-lettings-docker-build:9891ee25ce447303ef9d9a59cb732c5adf3d5ec1
```

# News board API
[![Run in Postman](https://run.pstmn.io/button.svg)](https://god.postman.co/run-collection/08663766e9ebcabc10a4#?env%5Bproduction%5D=W3sia2V5IjoiVVJMIiwidmFsdWUiOiJodHRwczovL2FsaXphcmluc3Rvbi1uZXdzLWJvYXJkLWFwaS5oZXJva3VhcHAuY29tIiwiZW5hYmxlZCI6dHJ1ZX0seyJrZXkiOiJwb3N0X2lkIiwidmFsdWUiOiIxIiwiZW5hYmxlZCI6dHJ1ZX0seyJrZXkiOiJjb21tZW50X2lkIiwidmFsdWUiOiIxIiwiZW5hYmxlZCI6dHJ1ZX1d)
[![Heroku](https://www.herokucdn.com/deploy/button.svg)](https://alizarinston-news-board-api.herokuapp.com)

## Setup

Use external services or start via Docker:
```
docker-compose up -d
```

Migrate database:
```
python manage.py migrate
```

Install fixtures:
```
python manage.py loaddata init
```

Run development server:
```
python manage.py runserver
```

Run celery beat & worker for periodic tasks:
```
celery -A config beat -l INFO
celery -A config worker -l INFO ([-P solo] for windows)
```

Use `BOARD_CONF` environment variable for custom config from `.ini` file in the `config` folder,
otherwise `config.ini` will be used. Sample config `config_default.ini` stored 
in the `config` folder.

Log in with credentials `admin / admin`.

## Documentation

Static snapshot of Postman collection: https://www.getpostman.com/collections/618103bf3631da9a53ba

Postman without environment: https://god.postman.co/run-collection/618103bf3631da9a53ba

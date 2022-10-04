# fastapi-asyncpg-alembic
## Depedency
All of depedency is available in *requrements.txt* file. This project is developing with python3.7 programming leanguage.

## Project Structure
    ./
    ├── alembic.ini
    ├── deliveries                     # Folder contains controller endpoints
    │   └── auth
    │       ├── controller.py
    │       ├── __init__.py
    │       └── schemas.py
    ├── configs                 # Folder contains all configs
    │   ├── application.py
    │   ├── database.py
    │   └── __init__.py
    ├── datasource                      # Folder db tools
    │    └── db
    │       └── async_pg.py
    ├── LICENSE
    ├── main.py                 # Main Program             
    ├── migrations              # Folder auto generating from alembic revision migrations
    │   ├── env.py
    │   ├── README
    │   ├── script.py.mako
    │   └── versions
    │        └── __init__.py
    ├── pkg                     # Folder additional package to extend feature
    │   └── env
    │       └──  __init__.py
    ├── README.md
    ├── repository              # Folder for db declarative (orm base)
    │   └── user
    │       ├── __init__.py
    │       └── models.py
    ├── requirements.txt
    ├── result.html
    ├── scripts                 # Folder contains all additional scripts
    │   ├── check_connection.py
    │   └──  create_secret.sh
    ├── .env.example
    .
    .


## Configuration
1. Copy [.env.example](.env.example) as [.env](.env)

```bash
cp .env.example .env
```

2. Below is available configurations:

| Key               | Description             | Values                       | Required |
|-------------------|-------------------------|------------------------------|----------|
| `SECRET_KEY_APPS` | Secret key for jwt      | string                       | ✓        |
| `PORT_APPS`       | Port apps while running | int, Default: 5000           |          |
| `HOST_APPS`       | Host apps while running | string, Default: 'localhost' |          |
| `HOST_DB`         | Server port             | Int                          | ✓        |
| `NAME_DB`         | Name database           | String                       | ✓        |
| `USER_DB`         | User database           | String                       | ✓        |
| `PASSWORD_DB`     | Password database       | string                       | ✓        |
| `PORT_DB`         | Port database           | String                       | ✓        |


## DB Migration
Metadata for database is there in repository folder.
### First Migrations

```bash
alembic revision --autogenerate -m "init"
```
### Update DB
```bash
alembic upgrade head
```

## Deployment
### Run The application

Using Makefile to setup development

1. Setup Dev

```shell
make setup-dev
```

2. Run development runtime

```shell
make dev
```

### Contributors ###
- Abdul Hamid

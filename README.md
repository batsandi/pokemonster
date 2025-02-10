# Run locally

## Postgres Docker Image
```
docker pull postgres
```
then run as
```
docker run -d --name pokemonster_postgres -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=1123QwER -e POSTGRES_DB=pokemonster_database -p 5432:5432 postgres
```

## Start project
create venv
install requirements.txt
apply migrations
runserver

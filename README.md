# Run locally

1. Postgres Docker Image
```
docker pull postgres
```
2. then run as
```
docker run -d --name pokemonster_postgres -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=1123QwER -e POSTGRES_DB=pokemonster_database -p 5432:5432 postgres
```

3. Start project
   - create venv
   - install requirements.txt
   - apply migrations
   - runserver

## Prod setup notes
Prerequisites:
- `aws profile (cli)`
- `eb cli`

Process:

```
eb init
```

Then
 ```
  eb create -db.engine postgres -db.i db.t3.micro -i t3.micro --single
  ```


> [!NOTE]
The `.ebextensions` folder contains the `.config` files for starting the wsgi server and running  migrations. The `.platform`  folder has the prebbuild script for the linux packages installation. `.elasticbeanstalk` is created when the `eb init`command runsthis

> [!WARNING]
Make sure to `eb terminate` and verify that the RDS instance is shut down
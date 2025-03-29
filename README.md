# Run locally

1. Postgres Docker Image
```
docker pull postgres
```
2. then run as
```
docker run -d --name pokemonster_postgres -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=1123QwER -e POSTGRES_DB=pokemonster_database -p 5432:5432 postgres
```

3. Rename `env.sample` to `.env`
> [!WARNING]
> The `.env` file will be loaded successfully in `settings.py` after you rename it and will overwrite the EB provided credentials in case you leave it in. 
>
> __Edit:__ Come to think of it, .env is gitignored, soo it shouldn't make it to the S3 bucket...

4. Start project
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
> Tested with Python 3.12

> [!WARNING]
> The superuser credentials are defined in the management command itself. If this ever goes to production for some strange reason, this should be handled using a `.env` file. default creds are:
> - super@user.com
>-  P4ssw0rd

> [!NOTE]
The `.ebextensions` folder contains the `.config` files for starting the wsgi server and running  migrations. The `.platform`  folder has the prebbuild script for the linux packages installation. `.elasticbeanstalk` is created when the `eb init`command runsthis


Alternatively, you can run the `eb create` command without the `-db` argument, which should fallback to the app using the SQLite engine and db.

 ```
  eb create -i t3.micro --single
  ```

Finally, 

```
eb terminate --all --force
```
To shut down the environment.

remove the `.elasticbeanstalk` dir

```bash
rm -rf .elasticbeanstalk
```

  > [!WARNING]
I believe that this will leave the EB application, as well as a snapshot of the deleted database instance available somewhere.
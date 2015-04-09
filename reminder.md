# Reminder

## Launch server
```
cd labrise/
source ../env/bin/activate
./manage.py runserver labri.se:8000
```

## View context on template
```
{% filter force_escape %}{% debug %}{% endfilter %}
```

## Database 
```
sudo su - postgres # connect to postgres UNIX user
psql               # postgresql CLI client
psql <dbname>      # postgresql CLI client
createdb <dbname>  # create a DB
dropdb <dbname>    # delete a DB
createuser <user>  # create a user
drop <user>        # user

GRANT ALL PRIVILEGES ON DATABASE labrise TO labrise;
CREATE EXTENSION postgis;
CREATE EXTENSION postgis_topology;

# postgresql's conf
/etc/postgresql/.../postgresql.conf
# Default port is 5432
```

## Django
```
./manage.py makemigrations <app>     # after models edit (once)
./manage.py migrate                  # after models edit
./manage.py runserver <address:port> # run server
./manage.py shell
```

## Sass
```
sass <input.scss> <output.css>
```

## Delete migrations files
```
find {,./*} -type d | grep migrations | xargs rm -rf
```
# Reminder

## Links


## Launch server
```
# easy way
cd labrise/
source ../env/bin/activate
sass assets/stylesheets/_bootstrap.scss assets/css/bootstrap.min.css # run only if scss has been changed
./manage.py collectstatic                                            # run only first time OR if any static file changed
./manage.py runserver labri.se:<port>

# dev way
cd labrise/
screen
	source ../env/bin/activate
	sass assets/stylesheets/_bootstrap.scss assets/css/bootstrap.min.css # run only if scss has been changed
	./manage.py collectstatic                                            # run only first time OR if any static file changed
	./manage.py syndb 													 # run only first time to setup DB
	./manage.py migrate 												 # run only if migrations needed (models edit)
	./manage.py runserver labri.se:8000
	Ctrl+A ... D                                                         # shortcut to go out of screen
	screen -r                                                            # re-open screen

# prod way
```

## View context on template
```
{% filter force_escape %}{% debug %}{% endfilter %}
```

## Database

Requirements: 
- postgresql >= 9.4
- postgis >= 2.1

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
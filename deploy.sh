#!/bin/bash
#
# ------------------------------
# Deploy script for Labri.se app
echo 'Deploy Labri.se'
#
#
# -----------------------
# Static files operations 
# Compile SASS files to static
echo 'Compile SASS files to static...'
rm -rf assets/css
mkdir assets/css
sass assets/stylesheets/_bootstrap.scss assets/css/bootstrap.min.css
echo 'Done.'
#
#
# -----------------
# Prepare to launch
# Prepare DB
echo 'syncdb: run ./manage.py syncdb'
./manage.py syncdb
echo 'makemigrations: run ./manage.py makemigrations'
./manage.py makemigrations
echo 'migrate: run ./manage.py migrate'
./manage.py migrate
#
# Collect static files
./manage.py collectstatic --noinput
#
#
# -------------
# Launch server
./manage.py runserver labri.se:8000


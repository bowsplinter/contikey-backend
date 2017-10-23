# dboard-backend

###Developer Installations

Install `virutalenv` and `mkvirtualenv`. `mkvirtualenv` is a wrapper around `virtualenv` and makes it easier to use but is optional.

Create virutal environment for project:

`mkvirtualenv <name>`

If you have both python 2 and 3 installed, use this to use python 3 instead:

`mkvirtualenv --python=/usr/local/bin/python3`

Clone and cd to directory and activate virutalenv with:

`workon <name>`

Install python packages with:

`pip install -r /path/to/requirements.txt`

Edit settings.py file with your local database information (create database for project using mysql)

To run projects

`python manage.py migrate`

`python manage.py runserver`



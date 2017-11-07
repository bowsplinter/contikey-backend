# dboard-backend

###Developer Installations

Install `virtualenv` and `virtualenvwrapper`. `virtualenvwrapper` is a wrapper around `virtualenv` and makes it easier to use but is optional.

Create virtual environment for project:

`mkvirtualenv <name>`

If you have both python 2 and 3 installed, use this to use python 3 instead:

`mkvirtualenv --python=/usr/local/bin/python3`

Clone and cd to directory and activate virtualenv with:

`workon <name>`

Install python packages with:

`pip install -r /path/to/requirements.txt`

Install MariaDB Server:

`brew install mariadb`

MariaDB is also compatible with the mySQL Workbench editor.
Launch the MySQL Workbench application and go to Database > Connect to Database (Ctrl+U) from the menu bar.
Enter the following details:

`Hostname: mydboard.cjivvjfjcng2.ap-southeast-1.rds.amazonaws.com`

`Port: 3306`

`Username: dboard`

`Password: db1234567`

Or if mySQL Workbench isn't working, run on terminal:

`mysql -h mydboard.cjivvjfjcng2.ap-southeast-1.rds.amazonaws.com -P 3306 -u dboard -p`
and enter `db1234567` when prompted for the password

To run projects

`python manage.py migrate`

`python manage.py runserver`

`eb open`

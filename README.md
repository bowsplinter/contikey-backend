# dboard-backend

### Developer Installations

Install `virtualenv` and `virtualenvwrapper`. `virtualenvwrapper` is a wrapper around `virtualenv` and makes it easier to use but is optional.

Clone this project and cd into it.

Create and activate virtual environment for project with:

`mkvirtualenv <name>`

If you have both python 2 and 3 installed, use this to use python 3 instead:

`mkvirtualenv --python=/usr/local/bin/python3 <name>`

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

### Usage

To run projects:

`python manage.py migrate`

`python manage.py runserver`
<<<<<<< HEAD
=======

`eb open`

To exit the virtual environment:
`deactivate`

To activate it in future uses:
`workon <name>`
>>>>>>> 277c452c0f0f6bbdde8acf22d944c7e86a4d2d8b

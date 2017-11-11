# dboard-backend

## Developer Installations

### Project setup

Install `virtualenv` and `virtualenvwrapper`. `virtualenvwrapper` is a wrapper around `virtualenv` and makes it easier to use but is optional.

Clone this project and cd into it.

Create and activate virtual environment for project:  
`mkvirtualenv <name>`

If you have both python 2 and 3 installed, use this to use python 3 instead:  
`mkvirtualenv --python=/usr/local/bin/python3 <name>`

Install python packages:  
`pip install -r /path/to/requirements.txt`

Run the project:  
`python manage.py runserver`

View the site at `http://127.0.0.1:8000`.

### Database setup

#### For local development:
Install MariaDB:  
`brew install mariadb`

Start MariaDB and its command line:  
`brew services start mariadb`  
`mysql -u root -p`

Enter your password when prompted. You should see the prompt:  
`MySQL [(none)]>`

Set up database and user:

```
> CREATE DATABASE db_name;
> CREATE USER username@localhost IDENTIFIED BY 'password'; 
> GRANT ALL PRIVILEGES ON db_name.* TO username@localhost;
> FLUSH PRIVILEGES;
```

Create a file `.env.py` in the root folder and paste the following into it, entering your credentials correspondingly. Port can be left as an empty string to use the default port number. This file is not tracked by git.

```
settings = {
    'RDS_DB_NAME': 'db_name',
    'RDS_USERNAME': 'username',
    'RDS_PASSWORD': 'password',
    'RDS_HOSTNAME': 'localhost',
    'RDS_PORT': '',
}
```

Apply migrations to create tables (in normal command line):  
`pip install sqlparse` this is needed to run raw SQL  
`python manage.py migrate`

Check that tables are created (in MariaDB command line):

```
MySQL [(none)]> USE db_name;
MySQL [db_name]> SHOW TABLES;
```

If you see a list of tables, congrats everything worked!!

#### For AWS:

MariaDB is also compatible with the mySQL Workbench editor.
Launch the MySQL Workbench application and go to Database > Connect to Database (Ctrl+U) from the menu bar.
Enter the following details:

```
Hostname: mydboard.cjivvjfjcng2.ap-southeast-1.rds.amazonaws.com
Port: 3306
Username: dboard
Password: db1234567
```

Or if mySQL Workbench isn't working, run on terminal:

`mysql -h mydboard.cjivvjfjcng2.ap-southeast-1.rds.amazonaws.com -P 3306 -u dboard -p`
and enter `db1234567` when prompted for the password

### Usage

To run projects:

`python manage.py migrate`

`python manage.py runserver`

`eb open`

To exit the virtual environment:
`deactivate`

To activate it in future uses:
`workon <name>`

To define the models and link it to endpoints, refer to http://www.django-rest-framework.org/tutorial/1-serialization/

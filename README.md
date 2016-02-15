# squiz
Quiz app description here.

## Setup
To run a local version of this django app:

Create a virtualenvironment, 'workon' it, then run;
```
pip install -r requirements.txt
```
This will install all of the dependencies needed by this app.



If you have made any changes to the database, run;
```
python manage.py makemigrations
```
This will create some migration files that tell django the difference between the current database and the models in models.py



To apply migrations or to create the databaser, type;
```
python manage.py migrate
```
This will make any migrations produced by ```makemigrations``` to the database.



Finally, to run the server, run;
```
python manage.py runserver
```
Then nativate to [localhost:8000](http://127.0.0.1:8000)

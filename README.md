# squiz
Paperless pub quiz.
Players can join quizzes easily and see where nearby quizzes are.
Hosts can create their own or use other user-created quizzes to then play at their venue.
## Setup
To run a local version of this django app:

Create a virtualenvironment, 'workon' it, then run;
```
pip install -r requirements.txt
```
This will install all of the dependencies needed by this app.


Navigate to the directory then to apply migrations or to create the database, type;
```
python manage.py migrate
```

Then run the population script
```
python pop.py
```


Finally, to run the server, run;
```
python manage.py runserver
```
Then nativate to [localhost:8000](http://127.0.0.1:8000)

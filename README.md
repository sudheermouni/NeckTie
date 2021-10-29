# NeckTie

# Choice of Framework & Library:
Django is the best framework for web applications, as it allows developers to use modules for faster development.
As a developer, you can make use of these modules to create apps, websites from an existing source. 
It speeds up the development process greatly, as you do not have to code everything from scratch.

#### Advantages over other framework
1. It fallows MVT architecture
2. it supports all types of databases
3. it has admin dashboard
4. more secure


Setup
-----

The django `python manage.py` commands only work after the
setup steps are completed.

Virtual Environment
-------------------

#### macOS

Create the virtualenv:
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```


#### Windows

Create virtualenv:
```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```


Tests
-----

To run tests, activate your virtual environment and run:
```
python manage.py test path_of_file
```


Running the Server Locally
--------------------------

To run the server locally, run the following commands:
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver localhost:8000
```

If the dependencies in the requirements.txt file change, then
you will need to re-install dependencies with pip. See the
troubleshooting section at the bottom of this document if you
get stuck.

Jwt Authentication:
------------------
Before viewing api we should be authenticated. For authentication purpose used **simplejwt**
```
pip install djangorestframework-simplejwt==4.4.0
pip install PyJWT==1.7.1
```
command prompt

Access token
```
http post http://127.0.0.1:8000/api/token/ username=sudheer password=123456
```
we should get access token. Then we need to pass token for access all api's
command prompt
```
http http://127.0.0.1:8000/v1/doctors "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM1NDc2NDEwLCJqdGkiOiIxNTdkNjE2MTZmZWU0OTYyYmM0NzMyYjQ5OWI5Y2RjMSIsInVzZXJfaWQiOjF9.2AwaH-Al_n2hOKpjBcXB6XTbNWJgZncGdS-IBMvbFR4"
```

Loading Fixtures
----------------
It will load sample data to the models
```
python manage.py loaddata necktieapp/fixtures/*.json
```

API Documentation
-----------------

To view API documentation, when running locally on port 8000, open:
 * http://localhost:8000/doctors
 * http://localhost:8000/patients


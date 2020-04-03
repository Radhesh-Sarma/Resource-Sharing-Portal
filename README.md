# Resource Sharing website

Web portal to help people connect with each other and share resources and goods.

## Installing
1.Clone the repo and configure the virtual environment

2. Set up the initial migration build the database.

```
$ sudo apt install postgresql postgresql-contrib
$ pip install django psycopg2
$ pip install django-allauth
$ pip install django-crispy-forms
$ pip install django-debug-toolbar
$ pip install pyyaml ua-parser user-agents
$ pip install django-user-agents
$ pip install captcha
$ pip install django-simple-captcha
$ pip install django-recaptcha
$ pip install django-ipware
$ python manage.py makemigrations
$ python manage.py migrate
```

3.  Create a superuser:

```
$ python3 manage.py createsuperuser
```

4.  Confirm everything is working:

```
$ python3 manage.py runserver
```

## Authors

* [Radhesh Sarma](https://github.com/Radhesh-Sarma) &nbsp;&nbsp;&nbsp;
* [Simran Sahni](https://github.com/Simran-Sahni)&nbsp;&nbsp;
* [Nikhil Mohan Krishna](https://github.com/samael042)&nbsp;&nbsp;
* [Abhiraj Singh](https://github.com/AbhirathS)&nbsp;&nbsp;&nbsp;&nbsp;

 * Special Thanks to [Pranjal Shukla](https://www.facebook.com/PataNahi0)&nbsp; for valuable feedback, suggestions
## To be added

 
## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**




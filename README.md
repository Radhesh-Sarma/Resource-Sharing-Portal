# Resource Sharing website

Web portal to help people connect with each other and share resources and goods.

## Getting Started
You need to install these :
- [_python_](https://www.python.org/downloads/source/)
- [_git_](https://git-scm.com/downloads/)
- [_pip_](https://pip.pypa.io/en/stable/installing/)

    
To download the repo use : 
```git
    git clone https://github.com/Radhesh-Sarma/Resource-Sharing-Website.git
```
## Installation 
1. Install Postgresql for your os

2. Install the virtual environment
```bash
    pip install pipenv
```
3. Activate the virtual env
```bash
    pipenv shell
```
4. Download the dependencies
```bash
    pipenv install
```
5.Set up the initial migration build the database.
```bash
  python manage.py makemigrations
  python manage.py migrate
```
6.  Create a superuser:
```bash
  python manage.py createsuperuser
```
7.  Confirm everything is working:
```bash
  python manage.py runserver
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



